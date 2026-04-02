#!/usr/bin/env python3
"""
Convert Markdown report to PDF
"""
import os
import sys

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from weasyprint import HTML
import markdown

def convert_md_to_pdf(md_file, pdf_file):
    """Convert markdown file to PDF"""
    
    # Read markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Add CSS for styling
    css = """
    @page {
        size: A4;
        margin: 2cm;
        @bottom-center {
            content: "Page " counter(page) " of " counter(pages);
            font-size: 10pt;
        }
    }
    body {
        font-family: Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        text-align: justify;
    }
    h1 {
        font-size: 24pt;
        text-align: center;
        color: #2c3e50;
        margin-top: 30pt;
        margin-bottom: 20pt;
    }
    h2 {
        font-size: 18pt;
        color: #34495e;
        border-bottom: 2px solid #3498db;
        padding-bottom: 5pt;
        margin-top: 25pt;
    }
    h3 {
        font-size: 14pt;
        color: #555;
    }
    p {
        margin-bottom: 12pt;
    }
    code {
        background-color: #f4f4f4;
        padding: 2pt 4pt;
        font-family: monospace;
    }
    pre {
        background-color: #f4f4f4;
        padding: 10pt;
        border-left: 3px solid #3498db;
        overflow-x: auto;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 15pt 0;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8pt;
        text-align: left;
    }
    th {
        background-color: #3498db;
        color: white;
    }
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 15pt auto;
    }
    ul, ol {
        margin-left: 20pt;
    }
    li {
        margin-bottom: 5pt;
    }
    blockquote {
        border-left: 4px solid #3498db;
        padding-left: 15pt;
        color: #666;
        font-style: italic;
    }
    """
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'codehilite'])
    
    # Wrap in full HTML document
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
    
    # Convert to PDF
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
