from plum import dispatch
from .version import VERSION
from .string_operations import format_tex_filename


def line_to_extracted_include_string(line, include_root_directory):
    if type(line) is str:
        return line
    elif type(line) is File:
        return "\\input{" + line.filename + "}"


class File:
    def __init__(self, root_directory: str, filename: str):
        self.root_directory = root_directory
        self.filename = filename

    @dispatch
    def __eq__(self, other) -> bool:
        try:
            return (self.root_directory, self.filename, self.lines,) == (
                other.root_directory,
                other.filename,
                other.lines,
            )
        except AttributeError:
            return False

    @dispatch
    def __repr__(self) -> str:
        return self.lines.__repr__()

    @dispatch
    def string_merged_lines(self) -> list:
        header_line = f'% <input src="{self.filename}" root="{self.root_directory}" version="{VERSION}">'
        footer_line = f'% </input src="{self.filename}" root="{self.root_directory}" version="{VERSION}">'
        output_lines = [header_line] + self.lines.copy() + [footer_line]
        output_lines = [
            line if type(line) is str else line.string_merged_inner()
            for line in output_lines
        ]
        return output_lines

    @dispatch
    def string_merged_inner(self) -> str:
        return "\n".join(self.string_merged_lines())

    @dispatch
    def string_merged_outer(self) -> str:
        output_lines = self.string_merged_lines()
        if output_lines[-1] != "":
            output_lines.append("")
        return "\n".join(output_lines)

    @dispatch
    def string_extracted_file(self, include_root_directory=False) -> str:
        return "\n".join(
            [
                line_to_extracted_include_string(line, include_root_directory)
                for line in self.lines
            ]
        )

    @dispatch
    def string_extracted_files_list(self, include_root_directory=False) -> list:
        output_list = [
            (format_tex_filename(self.filename), self.string_extracted_file())
        ]
        for line in self.lines:
            if type(line) is not str:
                output_list += line.string_extracted_files_list(include_root_directory)
        return output_list
