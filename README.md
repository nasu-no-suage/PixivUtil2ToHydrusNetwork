# PixivUtil2ToHydrusNetwork

[Nandaka/PixivUtil2](https://github.com/Nandaka/PixivUtil2)でダウンロードした画像ファイルにタグ付けて
[hydrusnetwork/hydrus](https://github.com/hydrusnetwork/hydrus)にインポートするために
JSONファイルをtxtファイルに変換するスクリプト

## 動作環境
python 3.6以上

## 使い方

## 使用する前に画像とJSONファイルのバックアップは必ずしておいてください。

### 1. Pixivutil2で画像をダウンロードする
このときconfig.iniで`writeimagejson = True`としてください。

### 2. このレポジトリをクローンするかファイルをダウンロードして一つのフォルダに纏めておくなどしてください。そして（PixivUtil2ToHydrusNetworkの）config.iniにPixivUtil2でのダウンロードフォルダを入力する。
### 3. CLI上で`python main.py`と入力する
するとファイルの名前がずらずらと出ますが、これで正常に動いています。

もしスクリプトが動かないという相談や、こうしてもらっては困るといった苦情、こうしたほうが良いなどの提案などあればご連絡ください。
