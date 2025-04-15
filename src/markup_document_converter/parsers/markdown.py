# src/markup_document_converter/parsers/markdown.py

from src.markup_document_converter.interfaces import Parser

class MarkdownParser(Parser):
    def parse(self, text: str):
        print("=== MarkdownParser output ===")
        print(text)
