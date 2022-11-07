from .version import VERSION


class File:
    def __init__(self, root_directory, filename):
        self.root_directory = root_directory
        self.filename = filename

    def __eq__(self, other):
        return (self.root_directory, self.filename, self.lines,) == (
            other.root_directory,
            other.filename,
            other.lines,
        )

    def string_merged(self) -> str:
        header_line = f'% <input src="{self.filename}" root="{self.root_directory}" version="{VERSION}">'
        footer_line = f'% </input src="{self.filename}" root="{self.root_directory}" version="{VERSION}">'
        output_lines = [header_line] + self.lines.copy() + [footer_line, ""]
        output_lines = [
            line if type(line) is str else line.string_merged() for line in output_lines
        ]
        return "\n".join(output_lines)
