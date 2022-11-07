from pytex_merge.internal_representation import File
from pytex_merge import read_extracted_file


def test_read_extracted_file():
    root_directory = "./tests/tex"
    f = read_extracted_file(root_directory, "main.tex")
    f_section_1 = File(root_directory, "sections/section_1.tex")
    f_section_1.lines = [
        "\\section{Introduction}",
        "",
        "This section is just there for testing purposes.",
        "",
    ]
    f_section_2 = File(root_directory, "sections/section_2.tex")
    f_section_2.lines = [
        "\\section{Background}",
        "",
        "This section is another section for testing purposes.",
        "",
    ]
    f_main = File(root_directory, "main.tex")
    f_main.lines = [
        "\\documentclass{amsart}",
        "\\begin{document}",
        f_section_1,
        f_section_2,
        "\\end{document}",
        "",
    ]
    assert f == f_main
