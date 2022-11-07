import os
from pytex_merge.read_extracted import read_extracted_file


def test_File_string_merged():
    root_directory = "./tests/tex"
    f = read_extracted_file(root_directory, "main.tex")
    with open(os.path.join(root_directory, "main_merged.tex"), "r") as file:
        data = file.read()
    assert f.string_merged() == data
