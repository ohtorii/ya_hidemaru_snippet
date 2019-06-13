# -*- coding: utf-8 -*-
"""
# Before
image foo.jpg 代替テキスト 画像タイトル
image 代替テキスト foo.jpg 画像タイトル
image 代替テキスト 画像タイトル foo.jpg

# After
![代替テキスト](foo.jpg "画像タイトル")
"""
import sys,os
import ya_hidemaru_snippet


def image_file(ext):
    import image_extensions
    return ext.lower() in image_extensions.image_extensions

def main(argv):
    import_path=os.path.normpath(ya_hidemaru_snippet.module_dir()+"\\markdown\\image\\")
    sys.path.append(import_path)

    first   =argv[1]
    second  =argv[2]
    third   =argv[3]

    other,ext=os.path.splitext(first)
    if image_file(ext):
        sys.stdout.write('![%s](%s "%s")' % (second,first,third))
        return ;

    other,ext=os.path.splitext(second)
    if image_file(ext):
        sys.stdout.write('![%s](%s "%s")' % (first,second,third))
        return ;

    other,ext=os.path.splitext(third)
    if image_file(ext):
        sys.stdout.write('![%s](%s "%s")' % (first,third,second))
        return ;

    sys.stdout.write('![%s](%s "%s")' % (first,second,third))


if __name__ == "__main__":
    main(sys.argv[1:])
