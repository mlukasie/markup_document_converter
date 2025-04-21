from src.markup_document_converter.converters.markdown_converter import (
    MarkdownConverter,
)


def print_ast(node, indent=0):
    prefix = "  " * indent
    print(f"{prefix}- {node.node_type}", end="")

    if node.attributes:
        attr_str = ", ".join(f"{k}={repr(v)}" for k, v in node.attributes.items())
        print(f" ({attr_str})")
    else:
        print()

    for child in node.children:
        print_ast(child, indent + 1)


def main():
    converter = MarkdownConverter()
    root = converter.to_AST("./tests/converters/basic.md")
    print_ast(root)
