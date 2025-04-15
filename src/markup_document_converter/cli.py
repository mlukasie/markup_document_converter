# src/markup_document_converter/cli.py

from markup_document_converter.parsers.markdown_parser import MarkdownParser

if __name__ == "__main__":
    with open("example.md", "r", encoding="utf-8") as f:
        text = f.read()

    parser = MarkdownParser()
    parser.parse(text)
