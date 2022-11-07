from pytex_merge.string_operations import string_find_wrapped_content, read_file_lines


def test_string_find_wrapped_content():
    string = "% \\input{test_string}"
    assert string_find_wrapped_content(string, "\\input{", "}") == "test_string"
    assert string_find_wrapped_content(string, "aaa", "bbb") is None


def test_read_file_lines():
    filename = "tests/tex/main.tex"
    assert read_file_lines(filename) == [
        "\\documentclass{amsart}",
        "\\begin{document}",
        "\\input{sections/section_1.tex}",
        "\\input{sections/section_2.tex}",
        "\\end{document}",
    ]
    assert read_file_lines(
        filename, lambda line: string_find_wrapped_content(line, "\\input{", "}")
    ) == [
        None,
        None,
        "sections/section_1.tex",
        "sections/section_2.tex",
        None,
    ]
