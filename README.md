# PixivUtil2ToHydrusNetwork

[Nandaka/PixivUtil2](https://github.com/Nandaka/PixivUtil2)でダウンロードした画像ファイルにタグ付けて
[hydrusnetwork/hydrus](https://github.com/hydrusnetwork/hydrus)にインポートするために
JSONファイルをtxtファイルに変換するスクリプト

## 使い方

## ある程度のテストはしていますが何が起こるかわかりませんので画像とJSONファイルのバックアップを必ずしておいてください。何が起こっても責任は取れません。

### 1. Pixivutil2で画像をダウンロードする
このときconfig.iniで`writeimagejson = True`としてください。

### 2. このレポジトリをクローンして（PixivUtil2ToHydrusNetworkの）config.iniにPixivUtil2で指定したダウンロードフォルダを入力する。
### 3. CLI上で`python main.py`とする

もしスクリプトが動かないという相談や、こうしてもらっては困るといった苦情、こうしたほうが良いなどの提案などあればご連絡ください。
