秀丸エディタの動的スニペット
========

- [開発の経緯](#開発の経緯)
- [特徴](#特徴)
- [マクロの導入方法](#マクロの導入方法)
- [ファイル構成](#ファイル構成)
- [動作環境のカスタマイズ](#動作環境のカスタマイズ)
- [スニペットのカスタマイズと新規作成](#スニペットのカスタマイズと新規作成)
- [動作環境](#動作環境)
- [更新履歴](#更新履歴)
- [連絡先](#連絡先)
- [謝辞](#謝辞)

# 開発の経緯

秀丸エディタには多くのスニペットマクロが公開されていまが、それら全ては**静的スニペット**展開です。<br>
**動的スニペット**展開を行いたくこのマクロを作成しました。

# 特徴

本マクロではスニペットに、
- [静的なスニペット]　テキストファイル
- [動的なスニペット]　秀丸マクロ・Python・VBScript・JavaScript・WindowsBatch

の両方を使用できます。<br>
従来の静的スニペットに加えて、可変個の入力に応じた**動的スニペット**を利用できます。

動的スニペットの動作は下記スクリーンショットで確認できます。

### スクリーンショット(その1 C/C++ basic)

![cpp main](ya_hidemaru_snippet/image/cpp_main.gif "cpp snippet")

### スクリーンショット(その2 C/C++ class)

![cpp class](ya_hidemaru_snippet/image/cpp_class.gif "cpp snippet")

### スクリーンショット(その3 C/C++ include guarder)

![cpp once](ya_hidemaru_snippet/image/cpp_once.gif "cpp snippet")

### スクリーンショット(その4 Python class)

![python snippet](ya_hidemaru_snippet/image/python.gif "python snippet")

### スクリーンショット(その5 MarkDown)

![markdown snippet](ya_hidemaru_snippet/image/markdown.gif "markdown snippet")

|コマンド|動作|
|:--:|:--:|
|toc	|目次(Table Of Contents)の挿入|
|table	|テーブルの挿入|
|image	|imageのテンプレートを挿入|
|link	|linkのテンプレートを挿入|

### スクリーンショット(その6 Hidemaru macro)

![hidemaru snippet](ya_hidemaru_snippet/image/hidemaru.gif "hidemaru snippet")

### スクリーンショット(その6 Text)

![Text snippet](ya_hidemaru_snippet/image/text.gif "text snippet")

|コマンド|動作|
|:--:|:--:|
|date|日にちの挿入|
|time|時間の挿入|
|@rep|文字列の繰り返しを挿入|

### スクリーンショット(その6 Command prompt)

![Command prompt](ya_hidemaru_snippet/image/cmd.gif "Command prompt")

|コマンド|動作|
|:--:|:--:|
|@cmd|コマンドプロンプトの実行|

コマンドプロンプトを実行して、

- カレントディレクトリのファイル一覧
- フォルダ構造
- 環境変数

などを取得できます。

# マクロの導入方法

全ファイルとフォルダを秀丸エディタのスクリプトディレクトリにコピーしてください。

	コピー後のディレクトリ構成
	hidemaru_macrodir
	│  ya_config_menu.mac
	│  ya_hidemaru_snippet.mac
	└─ya_hidemaru_snippet
	    ├─bonus
	    ├─doc
	    ├─image
	    ├─internal
	    └─snippets

## キーアサイン

`ya_hidemaru_snippet.mac` をキー割り当てして下さい。<br>
（キー割り当ての例）
- Ctrl-Enter
- Ctrl-P 
- Alt-Enter

ちなみに、私はCtrl-Enterに割り当てています。

ya_config_menu.mac は、この動的スニペットのマクロを更に便利にしたいときに利用します。<br>
なので、初めのうちは無理にキー割り当てをしなくても良いです。

# ファイル構成

|ファイル名|説明|
|:---|:---|
|ya_hidemaru_snippet.mac|動的スニペットマクロの本体|
|ya_config_menu.mac|スニペットを更に便利に使うためのおまけマクロ|

# 動作環境のカスタマイズ

`\ya_hidemaru_snippet\internal\config.ini` で以下カスタマイズが可能です。
- Pythonのバージョン(2 or 3)切り替え
- ファイル拡張子とスニペットのモードを紐付ける

# スニペットのカスタマイズと新規作成

スニペット定義は`ya_hidemaru_snippet\snippets\text-mode`フォルダ以下にあります。

まずは、以下ファイルを参照して頂くのが分かりやすいと思います。

|ファイル名|説明|
|:---|:---|
|email.txt|定型文を挿入する最も単純なスニペット|
|python-mode\if.txt|引数無しのスニペット|
|python-mode\if.%.txt|引数を一つ受け取るスニペット|
|c-mode\for.%.js|引数を一つ受け取りJavaScriptでスニペットを生成する|
|python-mode\def.%._.py|引数一つと可変個の引数を受け取りPythonでスニペットを生成する|
|c-mode\once.mac|秀丸マクロを利用したサンプル（秀丸エディタ固有の情報を取得してスニペットを生成します）|

# 動作環境

- 秀丸エディタ ver8以降
- でんがくDLL (http://www.ceres.dti.ne.jp/~sugiura/)
- ht_tools.dll (http://htom.in.coocan.jp/)

# 更新履歴

### 2018/12/02 ver 1.1.0
- テキストの選択範囲をスニペットとして認識するようにしました。
- 利用頻度の低いスニペットは削除して高いスニペットは機能強化を行いました。
- DLLの検索パスをhidemarudirとmacrodirの２箇所に変更しました。

### 2018/09/29 ver 1.0.0

- インストール方法やスニペットの定義方法などを追加

### 2012/09/24 ver 0.5.0

- GitHubにソースコードを公開

# 連絡先

<http://d.hatena.ne.jp/ohtorii/> <br>
<https://twitter.com/ohtorii> <br>
<https://github.com/ohtorii>

# 謝辞

- [TextMate](https://macromates.com/) スニペット書式をかなり参考にしました。
- [yasnippet](http://code.google.com/p/yasnippet/)
- [YASnippet Hidemarized](https://github.com/mobitan/yas/)
