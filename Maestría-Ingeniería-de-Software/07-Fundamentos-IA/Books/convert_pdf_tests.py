from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path


QUESTION_RE = re.compile(r"^(\d{1,2})\.\s+(.*)")
OPTION_RE = re.compile(r"^\s*([A-D])\.\s+(.*)")
TEST_FOOTER_RE = re.compile(r"Tema\s+(\d+)\.\s+Test", re.IGNORECASE)
THEME_RE = re.compile(r"^\s*Tema\s+(\d+)\s*$", re.IGNORECASE)
SECTION_RE = re.compile(r"^(\d+\.\d+)\.?\s+(.+)")


def run_pdftotext(pdf_path: Path, txt_path: Path) -> None:
    command = [
        "pdftotext",
        "-layout",
        "-enc",
        "UTF-8",
        str(pdf_path),
        str(txt_path),
    ]
    try:
        subprocess.run(command, check=True)
    except FileNotFoundError as exc:
        raise SystemExit(
            "No se encontró 'pdftotext'. Instala Poppler o Git for Windows, "
            "que suele incluir pdftotext.exe."
        ) from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"pdftotext falló con código {exc.returncode}") from exc


def strip_noise(line: str) -> str | None:
    text = line.rstrip()
    compact = text.strip()
    if not compact:
        return ""
    if compact.startswith("© Universidad Internacional de La Rioja"):
        return None
    if compact.startswith("Fundamentos de Inteligencia Artificial para Ingenieros de Software"):
        return None
    if re.match(r"^Tema\s+\d+\.\s+(Esquema|Ideas clave|A fondo)$", compact):
        return None
    return text


def normalize_text(text: str) -> str:
    replacements = {
        "ﬁ": "fi",
        "ﬂ": "fl",
        "\u00a0": " ",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return text


def clean_pages(raw_text: str) -> list[list[str]]:
    pages: list[list[str]] = []
    for page in normalize_text(raw_text).split("\f"):
        lines: list[str] = []
        for raw_line in page.splitlines():
            line = strip_noise(raw_line)
            if line is not None:
                lines.append(line)
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        if lines:
            pages.append(lines)
    return pages


def line_to_markdown(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return ""
    if THEME_RE.match(stripped):
        return f"# {stripped}"
    section_match = SECTION_RE.match(stripped)
    if section_match:
        return f"## {stripped}"
    if stripped in {"Índice", "Esquema", "Ideas clave", "A fondo", "Test"}:
        return f"## {stripped}"
    if TEST_FOOTER_RE.fullmatch(stripped):
        return ""
    if stripped.startswith("▸"):
        return f"- {stripped[1:].strip()}"
    if stripped.startswith("•"):
        return f"  - {stripped[1:].strip()}"
    return stripped


def write_book_markdown(pages: list[list[str]], output_path: Path, title: str) -> None:
    blocks = [f"# {title}", ""]
    for page in pages:
        previous_blank = False
        for line in page:
            md_line = line_to_markdown(line)
            if not md_line:
                if not previous_blank:
                    blocks.append("")
                previous_blank = True
                continue
            blocks.append(md_line)
            previous_blank = False
        blocks.append("")
        blocks.append("---")
        blocks.append("")
    output_path.write_text("\n".join(blocks).strip() + "\n", encoding="utf-8")


def page_topic(lines: list[str]) -> str | None:
    for line in lines:
        match = TEST_FOOTER_RE.search(line)
        if match:
            return match.group(1)
    return None


def parse_test_questions(pages: list[list[str]]) -> list[dict[str, object]]:
    questions: list[dict[str, object]] = []
    current_topic: str | None = None
    current_question: dict[str, object] | None = None
    current_option: dict[str, str] | None = None

    def finish_question() -> None:
        nonlocal current_question, current_option
        current_option = None
        if current_question and current_question.get("options"):
            questions.append(current_question)
        current_question = None

    for lines in pages:
        topic = page_topic(lines)
        meaningful = [line.strip() for line in lines if line.strip()]
        is_test_page = bool(topic and meaningful and meaningful[0] == "Test")
        if not is_test_page:
            continue
        current_topic = topic
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped == "Test" or "Tema " in stripped and ". Test" in stripped:
                continue
            if stripped.startswith("© "):
                continue

            question_match = QUESTION_RE.match(stripped)
            if question_match:
                finish_question()
                current_question = {
                    "topic": current_topic,
                    "number": int(question_match.group(1)),
                    "text": question_match.group(2).strip(),
                    "options": [],
                }
                continue

            option_match = OPTION_RE.match(line)
            if option_match and current_question:
                current_option = {
                    "letter": option_match.group(1),
                    "text": option_match.group(2).strip(),
                }
                current_question["options"].append(current_option)  # type: ignore[index]
                continue

            if current_question:
                if current_option:
                    current_option["text"] = f"{current_option['text']} {stripped}".strip()
                else:
                    current_question["text"] = f"{current_question['text']} {stripped}".strip()

    finish_question()
    return questions


def write_questions_markdown(questions: list[dict[str, object]], output_path: Path) -> None:
    lines = ["# Preguntas de test", ""]
    previous_topic: str | None = None
    for question in questions:
        topic = str(question["topic"])
        if topic != previous_topic:
            lines.append(f"## Tema {topic}")
            lines.append("")
            previous_topic = topic
        lines.append(f"{question['number']}. {question['text']}")
        for option in question["options"]:  # type: ignore[union-attr]
            lines.append(f"   - {option['letter']}. {option['text']}")
        lines.append("")
    output_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convierte un PDF a Markdown y extrae preguntas de test a otro Markdown."
    )
    parser.add_argument("pdf", type=Path, help="Ruta del PDF de entrada.")
    parser.add_argument(
        "--book-md",
        type=Path,
        default=None,
        help="Ruta del Markdown completo. Por defecto usa el nombre del PDF.",
    )
    parser.add_argument(
        "--questions-md",
        type=Path,
        default=None,
        help="Ruta del Markdown de preguntas. Por defecto agrega '-preguntas-test'.",
    )
    parser.add_argument(
        "--keep-raw",
        action="store_true",
        help="Guarda también el texto crudo extraído por pdftotext.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pdf_path = args.pdf.resolve()
    if not pdf_path.exists():
        print(f"No existe el PDF: {pdf_path}", file=sys.stderr)
        return 1

    book_md = args.book_md or pdf_path.with_suffix(".md")
    questions_md = args.questions_md or pdf_path.with_name(f"{pdf_path.stem}-preguntas-test.md")

    with tempfile.TemporaryDirectory() as tmpdir:
        raw_txt = Path(tmpdir) / f"{pdf_path.stem}.txt"
        run_pdftotext(pdf_path, raw_txt)
        raw_text = raw_txt.read_text(encoding="utf-8", errors="replace")
        if args.keep_raw:
            pdf_path.with_suffix(".raw.txt").write_text(raw_text, encoding="utf-8")

    pages = clean_pages(raw_text)
    write_book_markdown(pages, book_md, pdf_path.stem)
    questions = parse_test_questions(pages)
    write_questions_markdown(questions, questions_md)

    print(f"Markdown completo: {book_md}")
    print(f"Preguntas de test: {questions_md}")
    print(f"Preguntas extraídas: {len(questions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
