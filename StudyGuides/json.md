```json

{
  "$schema": "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json",
  "version": 4,
  "final_space": true,
  "osc99": true,
  "console_title_template": "{{ .Folder }}",

  "transient_prompt": {
    "background": "transparent",
    "foreground": "#A3A3A3",
    "template": "{{ .Shell }}> "
  },

  "palette": {
    "g0": "#0A0A0A",
    "g1": "#111111",
    "g2": "#171717",
    "g3": "#1F1F1F",
    "g4": "#262626",
    "g5": "#2E2E2E",
    "g6": "#3A3A3A",
    "g7": "#525252",
    "g8": "#A3A3A3",
    "g9": "#EDEDED",

    "gray_alpha_1": "#111111",
    "gray_alpha_2": "#171717",
    "gray_alpha_3": "#1F1F1F",
    "gray_alpha_4": "#262626",

    "blue": "#0091FF",
    "red": "#E5484D",
    "amber": "#F5A623",
    "green": "#30A46C",
    "purple": "#7C3AED",
    "vercel": "#0070F3",
    "vercel_dim": "#0055CC",

    "node": "#30A46C",
    "typescript": "#0091FF",
    "javascript": "#F5A623",
    "react": "#0091FF",
    "python": "#F5A623",
    "java": "#E5484D",
    "go": "#00B7C3",
    "rust": "#F5A623",
    "dotnet": "#7C3AED",
    "docker": "#0091FF"
  },

  "blocks": [
    {
      "type": "prompt",
      "alignment": "left",
      "segments": [
        {
          "type": "session",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:gray_alpha_1",
          "foreground": "p:g9",
          "template": " \uf120 {{ .HostName }} "
        },
        {
          "type": "path",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:gray_alpha_2",
          "foreground": "p:g9",
          "template": " {{ if .Segments.Git }}\uf418{{ else }}\uf07b{{ end }} {{ .Folder }} "
        },
        {
          "type": "text",
          "style": "powerline",
          "powerline_symbol": "\ue0b0",
          "background": "p:gray_alpha_3",
          "foreground": "p:g8",
          "template": "{{ if .Segments.Dotnet }} \ue77f .NET {{ end }}{{ if .Segments.Java }} \ue256 Java {{ end }}{{ if .Segments.Go }} \ue626 Go {{ end }}{{ if .Segments.Rust }} \ue7a8 Rust {{ end }}{{ if .Segments.Python }} \ue235 Py {{ end }}{{ if .Segments.Node }} \ue718 Node {{ end }}"
        },
        {
          "type": "git",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:vercel",
          "background_templates": [
            "{{ if or (.Working.Changed) (.Staging.Changed) }}p:amber{{ end }}",
            "{{ if and (gt .Ahead 0) (gt .Behind 0) }}p:purple{{ end }}",
            "{{ if and (not (or (.Working.Changed) (.Staging.Changed))) (gt .Behind 0) (eq .Ahead 0) }}p:green{{ end }}"
          ],
          "foreground": "#FFFFFF",
          "template": " \uf113 {{ .HEAD }}{{ if or (.Working.Changed) (.Staging.Changed) }} ●{{ else if .HEAD }} ✓{{ end }}{{ if gt .StashCount 0 }} \ueb4b {{ .StashCount }}{{ end }}{{ if and (gt .Ahead 0) (gt .Behind 0) }} ⇅ {{ .Ahead }}/{{ .Behind }}{{ else if gt .Ahead 0 }} ↑ {{ .Ahead }}{{ else if gt .Behind 0 }} ↓ {{ .Behind }}{{ end }} ",
          "options": {
            "fetch_status": true,
            "fetch_upstream_icon": true
          }
        }
      ]
    },

    {
      "type": "prompt",
      "alignment": "right",
      "segments": [
        {
          "type": "executiontime",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:g2",
          "foreground": "p:g9",
          "foreground_templates": ["{{ if gt .Ms 5000 }}p:amber{{ end }}"],
          "template": " \ueb62 {{ .FormattedMs }} ",
          "options": {
            "always_enabled": true,
            "threshold": 0,
            "style": "galvestonms"
          }
        },
        {
          "type": "text",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:red",
          "foreground": "p:g0",
          "template": " ERR {{ .Code }} ",
          "display_mode": "always",
          "background_templates": ["{{ if eq .Code 0 }}transparent{{ end }}"],
          "foreground_templates": ["{{ if eq .Code 0 }}transparent{{ end }}"]
        },
        {
          "type": "node",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:node",
          "foreground": "p:g0",
          "template": " \ue718 {{ .Full }} ",
          "display_mode": "files"
        },
        {
          "type": "python",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:python",
          "foreground": "p:g0",
          "template": " \ue235 {{ if .Error }}{{ .Error }}{{ else }}{{ if .Venv }}{{ .Venv }} {{ end }}{{ .Full }}{{ end }} ",
          "display_mode": "files"
        },
        {
          "type": "java",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:java",
          "foreground": "p:g0",
          "template": " \ue256 {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
          "display_mode": "files"
        },
        {
          "type": "go",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:go",
          "foreground": "p:g0",
          "template": " \ue626 {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
          "display_mode": "files"
        },
        {
          "type": "rust",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:rust",
          "foreground": "p:g0",
          "template": " \ue7a8 {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
          "display_mode": "files"
        },
        {
          "type": "dotnet",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:dotnet",
          "foreground": "p:g0",
          "template": " \ue77f {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
          "display_mode": "files"
        },
        {
          "type": "time",
          "style": "diamond",
          "leading_diamond": "\ue0b6",
          "trailing_diamond": "\ue0b4",
          "background": "p:g2",
          "foreground": "p:g9",
          "template": " \uf43a {{ .CurrentDate | date .Format }} ",
          "options": {
            "time_format": "Mon,15:04 PM"
          }
        }
      ]
    },

    {
      "type": "prompt",
      "alignment": "left",
      "newline": true,
      "segments": [
        {
          "type": "text",
          "style": "plain",
          "foreground_templates": [
            "{{ if gt .Code 0 }}p:red{{ else }}p:vercel{{ end }}"
          ],
          "template": "{{ if gt .Code 0 }}󰅙{{ else }}❯{{ end }} "
        }
      ]
    }
  ]
}
 
```

C

C:\Users\Dev\.