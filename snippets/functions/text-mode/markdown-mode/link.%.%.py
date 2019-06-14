# -*- coding: utf-8 -*-
"""
# Before
link https://www.google.com google
link google https://www.google.com

# After
[google](https://www.google.com)|

"""
import sys

def insert(title,link):
    sys.stdout.write("[%s](%s)%%|"%(title,link))

def main(argv):
    first=argv[1]
    second=argv[2]
    if "://" in first:
        insert(second,first)
    else:
        insert(first,second)

if __name__ == "__main__":
    main(sys.argv[1:])
