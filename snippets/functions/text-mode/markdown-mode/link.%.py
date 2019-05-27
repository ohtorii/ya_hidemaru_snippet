# -*- coding: utf-8 -*-
"""
# [1/2] Before
link https://www.google.com

# [1/2] After
[|Title](https://www.google.com)

# [2/2] Before
link google

# [1/2] After
[google](https://|)

"""
import sys

def main(argv):
    first=argv[1]
    if "://" in first:
        print("[%%|Title](%s)"%first)
    else:
        print("[%s](https://%%|)"%first)

if __name__ == "__main__":
    main(sys.argv[1:])
