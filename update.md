
# ????/??/?? ver 2.00.00

# 新機能

スニペットの一覧表示と引数入力を行うダイアログを用意しました。（空行でスニペットマクロを実行するとダイアログが起動します）<br>
どんなスニペットが利用できるのか分からない……という問題に対する解決策の１つです。

# スニペットファイル追加
- golang(.go)
	- main.txt
- 秀丸マクロ(.mac)
	- if#r.txt
	- if$r.txt
	- ifr.txt
	- ife.%.txt
	- ife.txt
	- ifee.%.txt
	- ifee.txt
- バッチファイル(.BAT)
	- date.txt
	- e.txt
	- e0.txt
	- e1.txt
	- for.txt
	- ford.txt
	- fordr.txt
	- forf.txt
	- forfr.txt
	- if.txt
	- ife.txt
	- main.txt
	- sleep.%.mac
	- sleep.mac
	- time.txt
	- touch.%.txt
	- touch.txt

スニペットの詳細はそれぞれのファイル内容を確認して下さい😅

# 設定ファイル(config.ini)の内容変更

Pythonのバージョン(2 or 3)に依存しないように内部処理を見直しました。
それに伴い、`config.ini`ファイルからPythonのバージョン情報に関する設定を削除しました。

# 非互換な更新（😱😱😱）

## ディレクトリの整理

ディレクトリが無駄に深かったので整理しました。

	（旧）
	hidemaru_macrodir
	├─ya_hidemaru_snippet.mac
	└─ya_hidemaru_snippet		  ← このディレクトリを削除しました。
	    └─internal
	        ├─config.ini
	        └─snippets

	（新）
	hidemaru_macrodir
	└─ya_hidemaru_snippet
	    ├─ya_hidemaru_snippet.mac
	    ├─config.ini
	    └─snippets

上記図は重要なフォルダとファイルのみ表示しています。

#### 旧バージョンからのバージョンアップ方法

- 旧バージョンのフォルダをリネームしてから新バージョンをインストールして下さい。
	- 新バージョンが正しく動作することを確認できたら、リネームしたフォルダを削除して下さい。
- あなたが独自に作成したスニペットファイルは対応するディレクトリ(snippets\functions\text-mode)に移動することで引き続き利用できます。

### スニペット仕様の変更（Pythonのみ）

- スニペットコード中で引数を受け取る方法をグローバル変数(argv[])からコマンドライン引数(sys.argv[])へ変更しました。

|区分|forループの例|
|:--:|--|
|(旧)|for index,value in enumerate(**argv[1:]**):|
|(新)|for index,value in enumerate(**sys.argv[2:]**):|


#### 詳細

	(旧) argv[]はグローバル変数。
		argv[0]	コマンド名
		argv[1]	引数
			:
			:
		argN[N]	引数
		
	(新) sys.argv[]はコマンドライン引数
		argv[0]	スニペットファイルへのパス   ←　新規追加の引数
		argv[1]	コマンド名
		argv[2]	引数
			:
			:
		argN[N]	引数

#### 具体例

以下のソースコードを参考にして下さい。<br>
*snippets\functions\text-mode\c-mode\c++-mode\template._.py*

### スニペット（コマンド名の変更）
- @rep → repeat
- @his → @history

# 最後に

互換性を失う変更はヒデマラーの皆さんにも私にもダメージ🤕があります。<br>
これが最後になるように努めます😘😘😘
