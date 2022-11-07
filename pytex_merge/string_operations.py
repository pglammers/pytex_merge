def format_tex_filename(filename):
    if filename[-4:] == ".tex":
        return filename
    else:
        return filename + ".tex"


def string_find_wrapped_content(input_string, string_start, string_stop):
    """Returns the content between the first occurrences of `string_start` and
    `string_stop`, or None if these two strings cannot be found in that order.

    Example:
    string = "% \\input{test_string}"
    assert string_find_wrapped_content(string, "\\input{", "}") == "test_string"
    """
    if type(input_string) is not str:
        return None
    position_start = input_string.find(string_start)
    position_stop = input_string.find(string_stop, position_start + len(string_start))
    if position_start >= 0 and position_stop >= 0:
        return input_string[position_start + len(string_start) : position_stop]
    else:
        return None


def read_file_lines(filename, processor=lambda line: line):
    with open(filename) as file:
        lines = [processor(line.rstrip()) for line in file]
        if lines[-1] != "":
            lines.append("")
    return lines
