# -*- coding: utf-8 -*-
"""
# Description:GitHub Flavored Markdown(GFM)

# Format
table column row

=========
# Example
=========
# before
table 3 2

# after
header1|header2|header3|
|:--:|:--:|:--:|
|a1|a2|a3|
|b1|b2|b3|
"""
import sys
import os
import ya_hidemaru_snippet

def main(argv):
    import_path=os.path.normpath(ya_hidemaru_snippet.module_dir()+"\\markdown\\table\\")
    sys.path.append(import_path)

    import create_table
    create_table.main(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
