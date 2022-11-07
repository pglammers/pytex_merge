import os
from plum import dispatch
from .version import VERSION
from .internal_representation import File
from .string_operations import (
    format_tex_filename,
    string_find_wrapped_content,
    read_file_lines,
)


def extract_tags(line):
    return (
        string_find_wrapped_content(line, 'src="', '"'),
        string_find_wrapped_content(line, 'root="', '"'),
        string_find_wrapped_content(line, 'version="', '"'),
    )


@dispatch
def in_line(line, string: str):
    if type(line) is File:
        return False
    elif type(line) is str:
        return string in line
    else:
        raise Exception


@dispatch
def find_input_tag(lines: list, root_directory: str) -> tuple:
    status = 0
    k, start = next(
        x for x in enumerate(lines) if string_find_wrapped_content(x[1], "<input", ">")
    )
    l, stop = next(
        x for x in enumerate(lines) if in_line(x[1], start.replace("<input", "</input"))
    )
    return k, l, extract_tags(start)


def process_input_tag(lines: list, root_directory: str) -> list:
    k, l, tags = find_input_tag(lines, root_directory)
    src, root, version = tags
    assert root == root_directory
    assert version == VERSION
    new_file = File(root_directory, src)
    new_file.lines = process_all_input_tags(lines[k + 1 : l], root_directory)
    new_lines = lines[:k] + [new_file] + lines[l + 1 :]
    return new_lines


def process_all_input_tags(lines: list, root_directory: str) -> list:
    finished = False
    while not finished:
        try:
            lines = process_input_tag(lines, root_directory)
        except StopIteration:
            finished = True
    return lines


@dispatch
def read_merged_file(root_directory: str, filename: str) -> File:
    lines = read_file_lines(os.path.join(root_directory, format_tex_filename(filename)))
    f = File(root_directory, filename)
    return process_all_input_tags(lines, root_directory)[0]
