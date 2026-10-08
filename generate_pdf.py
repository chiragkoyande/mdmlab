import markdown
from weasyprint import HTML
import os

ARTIFACT_DIR = "/home/chiragk/.gemini/antigravity-cli/brain/f04517f0-199f-431e-bcaf-53ee48dd5466"
IMG_DIR = "/home/chiragk/mdmlab/outputs"
OUTPUT_PDF = "/home/chiragk/mdmlab/WMC_Lab_Experiments_3_to_10_Output.pdf"

# Read the markdown
md_path = os.path.join(ARTIFACT_DIR, "WMC_Lab_Experiments_3_to_10_Output.md")
with open(md_path, "r") as f:
    md_content = f.read()

# Replace artifact dir image paths with absolute file:// URIs for weasyprint
md_content = md_content.replace(
    f"({ARTIFACT_DIR}/",
    f"(file://{ARTIFACT_DIR}/"
)

# Convert markdown to HTML
html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

html_full = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @page {{
        size: A4;
        margin: 1.5cm;
    }}
    body {{
        font-family: 'DejaVu Sans', 'Liberation Sans', Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.5;
        color: #222;
    }}
    h1 {{
        font-size: 18pt;
        text-align: center;
        border-bottom: 2px solid #333;
        padding-bottom: 8px;
        margin-top: 0;
    }}
    h2 {{
        font-size: 14pt;
        color: #1a1a6e;
        border-bottom: 1px solid #888;
        padding-bottom: 4px;
        page-break-before: always;
    }}
    h2:first-of-type {{
        page-break-before: avoid;
    }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin: 12px 0;
        font-size: 10pt;
    }}
    th, td {{
        border: 1px solid #555;
        padding: 6px 10px;
        text-align: left;
    }}
    th {{
        background-color: #e0e0f0;
        font-weight: bold;
    }}
    tr:nth-child(even) {{
        background-color: #f5f5f5;
    }}
    img {{
        max-width: 100%;
        display: block;
        margin: 10px auto;
    }}
    pre {{
        background-color: #f4f4f4;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 9pt;
        overflow-x: auto;
        white-space: pre-wrap;
        word-wrap: break-word;
    }}
    code {{
        font-family: 'DejaVu Sans Mono', 'Liberation Mono', monospace;
        font-size: 9pt;
    }}
    hr {{
        border: none;
        border-top: 1px solid #aaa;
        margin: 20px 0;
    }}
    strong {{
        color: #1a1a6e;
    }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

HTML(string=html_full).write_pdf(OUTPUT_PDF)
print(f"PDF created: {OUTPUT_PDF}")
