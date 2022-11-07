# pytex_merge

## Merging files
```
from pytex_merge import read_extracted_file


file = read_extracted_file(".", "main.tex")
file_merged = file.string_merged_outer()
```
The variable `file_merged` is a string which can be processed in any way.

## Extracting merged files
```
from pytex_merge import read_merged_file


file = read_merged_file(".", "main_merged.tex")
file_extracted_list = file.string_extracted_files_list()
```
The variable `file_extracted_list` is a list of pairs where the first element
denotes the file name and where the second element is a data string.

## Todo
- [ ] Add support for custom root directories.
