from pytex_merge import read_extracted_file, read_merged_file


def test_read_extracted_file():
    root_directory = "./tests/tex"
    f = read_extracted_file(root_directory, "main.tex")
    f2 = read_merged_file(root_directory, "main_merged.tex")
    assert f == f2
