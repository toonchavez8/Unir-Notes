```ts
const vowels: ReadonlySet<string> = new Set(["a", "e", "i", "o", "u"]);

  

const countVowels = (word: string): number =>

    [...word].filter((char) => vowels.has(char)).length;

  

export function flippedy(input: string): string {

    if (!input) return input;

  

    const words = input.split(" ");

  

    const firstCount = countVowels(words[0]);

  

    const NewInput = words

        .map((word, index) =>

            index === 0 || countVowels(word) !== firstCount

                ? word

                : [...word].reverse().join(""),

        )

        .join(" ");

  

    return NewInput;

}
```