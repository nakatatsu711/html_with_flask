## 概要
ヤフオクから商品情報をスクレイピングします。  
また、スクレイピングした情報をブラウザで見れるようにWebアプリ化します。

<br>

ヤフオクから残り時間が24時間以内のオークションのみを取得します。

オークションの商品情報をスクレイピングします。  
取得した商品情報をブラウザで見れるように、Flaskを使用してWebアプリ化します。



## システム環境
以下で動作確認済みです。  
OS：macOS 10.15.7  
Python：3.6.9



## 実行方法
### ライブラリインストール
以下の2通りの方法がありますので、どちらかでインストールしてください。

```
$ pip install selenium
$ pip install lxml
$ pip install cssselect
$ pip install requests
$ pip install Flask
```
```
$ pip install -r requirements.txt
```


### ChromeDriverについて
ブラウザはGoogleChromeを使用します。  
ブラウザを自動操作するためにChromeDriverを使用します。  
以下から自分のGoogleChromeと同じバージョンのドライバーをダウンロードします。  
[ChromeDriverのダウンロードはこちら](https://sites.google.com/a/chromium.org/chromedriver/downloads)

ChromeDriverをダウンロードしたら解凍して、任意の場所に配置します。  
そして、`scraping_yahooauc.py`の`chromedriver_path`のところに自分がダウンロードした場所を指定します。


### 実行
コマンドラインで実行します。  
実行するとまずヤフオクをスクレイピングして、商品情報を取得します。  
スクレイピング終了後、`http://127.0.0.1:5000/`にアクセスします。
```
$ python html_with_flask.py
```
