秀丸エディタの動的スニペット
========

# 開発の経緯
秀丸エディタには多くのスニペットマクロが公開されていまが、自分の考えに合致したマクロが無いためこのマクロを作成しました。

# 特徴
本マクロではスニペット定義に、
- [静的なスニペット]テキストファイル
- [動的なスニペット]秀丸マクロ・Python・VBScript・JavaScript・WindowsBatch

を使用できます。<br>
従来の静的なスニペットに加えて、可変個の入力に応じた**動的なスニペット**を定義できます。

動的なスニペットは下記スクリーンショットで確認できます。

### スクリーンショット(その1 C/C++ basic)
![cpp main](http://cdn-ak.f.st-hatena.com/images/fotolife/o/ohtorii/20110805/20110805181101.gif?1312535670 "cpp snippet")

### スクリーンショット(その2 C/C++ class)
![cpp class](http://cdn-ak.f.st-hatena.com/images/fotolife/o/ohtorii/20110805/20110805181100.gif?1312535644 "cpp snippet")

### スクリーンショット(その3 C/C++ include guarder)
![cpp once](http://cdn-ak.f.st-hatena.com/images/fotolife/o/ohtorii/20110805/20110805181059.gif?1312535961 "cpp snippet")

### スクリーンショット(その4 Python class)
![python snippet](http://cdn-ak.f.st-hatena.com/images/fotolife/o/ohtorii/20110805/20110805181058.gif?1312535978 "python snippet")


# マクロのインストールと設定方法
全ファイルとフォルダを秀丸のスクリプトディレクトリにコピーしてください。

## キーアサイン
`ya_hidemaru_snippet.mac` をキー割り当てして下さい。<br>
（キー割り当ての例）
- Ctrl-Enter
- Ctrl-P 
- Alt-Enter

ちなみに、私はCtrl-Enterに割り当てています。

ya_config_menu.mac は、この動的スニペットマクロを更に便利に使う場合に利用します。<br>
なので、初めのうちは無理にキー割り当てをしなくても良いです。

# ファイル構成
|ファイル名|説明|
|:---|:---|
|ya_hidemaru_snippet.mac|動的スニペットマクロの本体|
|ya_config_menu.mac|更に便利に使うためのマクロ（おまけマクロ）|

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
### 2018/09/29 ver 1.0.0
- インストール方法やスニペットの定義方法などを追加
### 2012/09/24 ver 0.5.0
- GitHubにソースコードを公開

# 連絡先
<http://d.hatena.ne.jp/ohtorii/> <br>
<https://twitter.com/ohtorii>
