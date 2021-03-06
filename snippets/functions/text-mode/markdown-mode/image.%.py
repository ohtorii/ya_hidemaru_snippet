﻿# -*- coding: utf-8 -*-
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
import ya_hidemaru_snippet

def image_file(ext):
    import image_extensions
    return ext.lower() in image_extensions.image_extensions

def main(argv):
    import_path=os.path.normpath(ya_hidemaru_snippet.module_dir()+"\\markdown\\image\\")
    sys.path.append(import_path)
    
    first=argv[1]
    other,ext=os.path.splitext(first)
    if image_file(ext):
        sys.stdout.write('![%%|代替テキスト](%s "画像タイトル")' % first)
        return ;
    
    sys.stdout.write('![%s](%%|foo.jpg "%s")' % (first,first))


if __name__ == "__main__":
    main(sys.argv[1:])
