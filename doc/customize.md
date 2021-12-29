# 動作環境のカスタマイズ

`config.ini` で以下のカスタマイズが可能です。
- python.exeへのファイルパス
- ファイル拡張子とスニペットモードを紐付ける

以下は`config.ini`のファイル内容です。
```ini
;
;Shift-Jis
;

[config]
.txt=text-mode
.doc=text-mode
.text=text-mode
.bat=text-mode\bat-mode
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

[snippets]
;
;ユーザー定義のスニペットパス
;user_path[0-9]で指定します。
;
;user_path0=%USERPROFILE%\ya_hidemaru_snippets\
;	:
;	:
;user_path9=D:\projects\FPS-Game\snippets\

[python]
;exe="C:\Python27\python.exe"
;exe="C:\Python32\python.exe"
exe="python.exe"

[new_file]
;新規ファイル（拡張子無し）の時に使用するスニペットモード
ext=".txt"

```


# ユーザー定義のスニペットパス

ユーザー定義のスニペットフォルダを10カ所まで登録できます。

## スニペットファイルの検索順

↑優先順位高い

- user_path0
- ...省略...
- user_path9
- 組み込みのスニペット

↓優先順位低い

## スニペットフォルダの構成

組み込みスニペットのフォルダ構成と同じにしてください。

	hidemaru_macrodir
	  └─ya_hidemaru_snippet
	     └─snippets　←　詳しくはこのフォルダ以下を参照してください。


# その他

- iniファイルなので文字コードはShift-Jisです。
- Pythonを利用したスニペットが動かないときは、[python]セクションをご自身の環境に合わせて修正して下さい。
