# SUGUMI-WEB

## SUGUMI-WEB
SUGUMIのWEB版

## 導入
コマンドプロンプトで以下のコマンドを実行する
```
git clone https://github.com/AtsushiUtsumi/sugumi_web.git
pip install pytest,python-dotenv,injector,psycopg2-binary,flask_wtf
sudo apt install libpq-dev
```

## リンク
[メモ](document/NOTE.md)  
[TODOリスト](document/TODO.md)

## 不具合

## 次にやること
- ドキュメントからDB
- DBからドキュメント
- この作業が明日以降の作業を軽減してくれるのか
- Pythonであることを活かした方法か?AI使うメリットを活かせる?
- レンタルサーバで試しに動作してみるか?
- ベイズ推論
- E資格
- 業務内容にマッチした内容なのか
- 画面毎にタスクが来る職場とは相性が悪いのでは?
- このアプリケーションのドキュメントをマークダウンで用意する

## chatGPTで生成した画像
<img src="document/image/プログラマ.png" width="400">

## injectorについて

### Injector
依存注入を行う。  

### Binder
ここで抽象クラスと具象クラスの紐付けを行う。  

### Provider
依存を提供する主体。  

### Module
Binderで紐付けてModuleでBinderを束ねる。  
Moduleは環境毎に変えるのかも(本番環境、テスト環境みたいな)  
