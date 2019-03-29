# 動作環境のカスタマイズ

`config.ini` で以下のカスタマイズが可能です。
- python.exeへのファイルパス
- ファイル拡張子とスニペットモードを紐付ける

以下は`config.ini`のファイル内容です。
```ini
[config]
.txt=text-mode
.doc=text-mode
.text=text-mode
.c=text-mode\c-mode
.h=text-mode\c-mode\c++-mode
.cpp=text-mode\c-mode\c++-mode
.hpp=text-mode\c-mode\c++-mode
.inl=text-mode\c-mode\c++-mode
.cs=text-mode\c-mode\csharp-mode
.py=text-mode\python-mode
.pl=text-mode\perl-mode
.php=text-mode\php-mode
.html=text-mode\html-mode
.htm=text-mode\html-mode
.md=text-mode\markdown-mode
.fx=text-mode\fx-mode
.cg=text-mode\fx-mode
.cgfx=text-mode\fx-mode
.hlsl=text-mode\fx-mode
.mac=text-mode\hidemaru-macro-mode
.cu=text-mode\c-mode\cuda-mode
.bat=text-mode
.go=text-mode\go-mode

[python]
;exe="C:\Python27\python.exe"
;exe="C:\Python32\python.exe"
exe="python.exe"

[new_file]
;新規ファイル（拡張子無し）の時に使用するスニペットモード
ext=".txt"
```

Pythonを利用したスニペットが動かないときは、[python]セクションをご自身の環境に合わせて修正して下さい。
