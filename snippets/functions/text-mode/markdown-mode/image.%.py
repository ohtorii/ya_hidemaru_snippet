# -*- coding: utf-8 -*-
"""
# [1/2] Before
image foo.jpg


# [1/2] After
![|代替テキスト](foo.jpg "画像タイトル")


# [2/2] Before
image 花の画像

# [2/2] After
![花の画像](|foo.jpg "花の画像")

"""
import sys,os

_image_extensions=set(
    (".bmp",
    ".gif",
    ".jpg",
    ".jpeg",
    ".jpf",
    ".jxr",
    ".webp",
    ".png",
    ".apng",
    ".svg")
)


def image_file(ext):
    return ext.lower() in _image_extensions

def main(argv):
    first=argv[1]
    other,ext=os.path.splitext(first)
    if image_file(ext):
        print('![%%|代替テキスト](%s "画像タイトル")' % first)
    else:
        print('![%s](%%|foo.jpg "%s")' % (first,first))

if __name__ == "__main__":
    main(sys.argv[1:])
