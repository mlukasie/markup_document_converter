from markup_document_converter.converters.base_converter import BaseConverter
import markup_document_converter.ast as ast


class TypstConverter(BaseConverter):
    def convert_default(self, node: ast.ASTNode) -> str:
        pass

    def convert_document(self, document: ast.Document) -> str:
        chidren_result = "\n".join([child.convert(self) for child in document.children])
        return chidren_result

    def convert_heading(self, heading: ast.Heading) -> str:
        chidren_result = "".join([child.convert(self) for child in heading.children])
        return f"{'=' * heading.level} {chidren_result}"

    def convert_bold(self, bold: ast.Bold) -> str:
        chidren_result = "".join([child.convert(self) for child in bold.children])
        return f"*{chidren_result}*"

    def convert_italic(self, italic: ast.Italic) -> str:
        chidren_result = "".join([child.convert(self) for child in italic.children])
        return f"_{chidren_result}_"

    def convert_strike(self, strike: ast.Strike) -> str:
        chidren_result = "".join([child.convert(self) for child in strike.children])
        return f"#strike[{chidren_result}]"

    def convert_text(self, text: ast.Text) -> str:
        return text.text

    def convert_paragraph(self, paragraph: ast.Paragraph) -> str:
        pass

    def convert_line_break(self, line_break: ast.LineBreak) -> str:
        return

    def convert_blockquote(self, blockquote: ast.Blockquote) -> str:
        pass

    def convert_list(self, list_node: ast.List) -> str:
        pass

    def convert_list_item(self, list_item: ast.ListItem) -> str:
        pass

    def convert_code_block(self, code_block: ast.CodeBlock) -> str:
        pass

    def convert_inline_code(self, inline_code: ast.InlineCode) -> str:
        pass

    def convert_image(self, image: ast.Image) -> str:
        pass

    def convert_link(self, link: ast.Link) -> str:
        pass

    def convert_horizontal_rule(self, horizontal_rule: ast.HorizontalRule) -> str:
        pass

    def convert_table(self, table: ast.Table) -> str:
        pass

    def convert_table_row(self, table_row: ast.TableRow) -> str:
        pass

    def convert_table_cell(self, table_cell: ast.TableCell) -> str:
        pass

    def convert_task_list_item(self, task_list_item: ast.TaskListItem) -> str:
        pass
