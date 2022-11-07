import os
from pytex_merge.read_extracted import read_extracted_file
from pytex_merge.internal_representation import File


def test_File___eq__():
    f = File("a", "b")
    f.lines = []
    assert f == f
    assert f != 1


def test_File_string_merged():
    root_directory = "./tests/tex"
    f = read_extracted_file(root_directory, "main.tex")
    with open(os.path.join(root_directory, "main_merged.tex"), "r") as file:
        data = file.read()
    assert f.string_merged_outer() == data


def test_File_string_extracted_file():
    root_directory = "./tests/tex"
    f = read_extracted_file(root_directory, "main.tex")
    with open("tests/tex/main.tex", "r") as file:
        f_original = file.read()
    assert f.string_extracted_file() == f_original


def test_File_string_extracted_files():
    root_directory = "./tests/tex"
    f = read_extracted_file(root_directory, "main.tex")
    files_list = f.string_extracted_files_list()
    for name, data in files_list:
        with open(f"tests/tex/{name}", "r") as file:
            f_original = file.read()
        assert data == f_original
