import os
from plum import dispatch
from .internal_representation import File
from .string_operations import (
    format_tex_filename,
    string_find_wrapped_content,
    read_file_lines,
)


def read_extracted_line(line: str, root_directory: str):
    try_input = string_find_wrapped_content(line, "\\input{", "}")
    if try_input is None or line.find("%") != -1:
        return line
    else:
        return read_extracted_file(root_directory, try_input)


@dispatch
def read_extracted_file(root_directory: str, filename: str) -> File:
    lines = read_file_lines(
        os.path.join(root_directory, format_tex_filename(filename)),
        lambda line: read_extracted_line(line, root_directory),
    )
    f = File(root_directory, filename)
    f.lines = lines
    return f
