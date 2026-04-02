#!/usr/bin/env python3
"""
Convert Markdown report to PDF with proper formatting
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from weasyprint import HTML
import markdown

def convert_md_to_pdf(md_file, pdf_file):
    """Convert markdown file to PDF with proper formatting"""
    
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    css = """
    @page {
        size: A4;
        margin: 2.5cm 2cm 2.5cm 2cm;
    }
    @page first {
        margin: 2.5cm 2cm 2.5cm 2cm;
    }
    @page :left {
        margin: 2.5cm 2.5cm 2.5cm 2cm;
    }
    @page :right {
        margin: 2.5cm 2cm 2.5cm 2.5cm;
    }
    body {
        font-family: 'Times New Roman', Times, serif;
        font-size: 12pt;
        line-height: 1.8;
        text-align: justify;
        color: #1a1a1a;
    }
    h1 {
        font-size: 28pt;
        text-align: center;
        color: #1a1a1a;
        font-weight: bold;
        margin-top: 0pt;
        margin-bottom: 30pt;
        page-break-after: always;
        border-bottom: 3px double #333;
        padding-bottom: 15pt;
    }
    h2 {
        font-size: 18pt;
        text-align: left;
        color: #2c3e50;
        font-weight: bold;
        border-bottom: 2px solid #3498db;
        padding-bottom: 8pt;
        margin-top: 30pt;
        margin-bottom: 15pt;
        page-break-after: avoid;
        page-break-inside: avoid;
    }
    h3 {
        font-size: 14pt;
        color: #34495e;
        font-weight: bold;
        margin-top: 20pt;
        margin-bottom: 10pt;
        page-break-after: avoid;
    }
    p {
        margin-top: 8pt;
        margin-bottom: 8pt;
        text-indent: 0.5in;
        text-align: justify;
    }
    p.no-indent {
        text-indent: 0;
    }
    code {
        font-family: 'Courier New', monospace;
        font-size: 10pt;
        background-color: #f5f5f5;
        padding: 2pt 4pt;
        border: 1px solid #ddd;
    }
    pre {
        font-family: 'Courier New', monospace;
        font-size: 9pt;
        background-color: #f8f8f8;
        padding: 12pt;
        border: 1px solid #ccc;
        border-left: 4px solid #3498db;
        white-space: pre-wrap;
        margin: 15pt 0;
        page-break-inside: avoid;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20pt 0;
        page-break-inside: avoid;
    }
    th, td {
        border: 1px solid #333;
        padding: 10pt 12pt;
        text-align: left;
    }
    th {
        background-color: #2c3e50;
        color: white;
        font-weight: bold;
        text-align: center;
    }
    tr:nth-child(even) {
        background-color: #f5f5f5;
    }
    img {
        max-width: 90%;
        height: auto;
        display: block;
        margin: 20pt auto;
        page-break-inside: avoid;
    }
    ul, ol {
        margin-left: 40pt;
    }
    li {
        margin-bottom: 6pt;
    }
    blockquote {
        border-left: 4px solid #3498db;
        padding-left: 15pt;
        margin: 15pt 30pt;
        color: #555;
        font-style: italic;
        background-color: #f9f9f9;
        padding: 10pt 15pt;
    }
    hr {
        border: none;
        border-top: 1px solid #ccc;
        margin: 30pt 0;
    }
    .center {
        text-align: center;
    }
    .bold {
        font-weight: bold;
    }
    """
    
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'codehilite', 'toc'])
    
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Brain Tumor Detection Report</title>
        <style>{css}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    HTML(string=full_html).write_pdf(pdf_file)
    print(f"PDF saved to: {pdf_file}")

if __name__ == "__main__":
    md_file = "report/Brain_Tumor_Detection_Report.md"
    pdf_file = "report/Brain_Tumor_Detection_Report.pdf"
    
    if not os.path.exists(md_file):
        print(f"Error: {md_file} not found!")
        sys.exit(1)
    
    convert_md_to_pdf(md_file, pdf_file)
    print("Conversion complete!")
