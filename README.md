# PixivUtil2ToHydrusNetwork

[Nandaka/PixivUtil2](https://github.com/Nandaka/PixivUtil2)でダウンロードした画像ファイルを
[hydrusnetwork/hydrus](https://github.com/hydrusnetwork/hydrus)にPixivサイト上で画像についているタグと関連付けてインポートするために
JSONファイルから画像ファイル一枚一枚ごとにタグの記載されたtxtファイルを作成するスクリプト

```
"12345_p0 - sample.png" または "12345_p0 - sample.jpg"と
"12345_p0 - sample.json" から
"12345_p0 - sample.png.txt" または "12345_p0 - sample.jpg.txt"を作成
```
## 動作環境
- Arch Linux
- Windows 10
- python 3.6以上
で動作確認

## 使い方

## 使用する前に画像とJSONファイルのバックアップは必ずしておいてください。

### 1. Pixivutil2で画像をダウンロードする
このときconfig.iniで`writeimagejson = True`としてください。

### 2. このレポジトリをクローンするかファイルをダウンロードして一つのフォルダに纏めておくなどしてください。そして（PixivUtil2ToHydrusNetworkの）config.iniにPixivUtil2でのダウンロードフォルダを入力する。
### 3. CLI上で(Windows 10の場合PowerShellやcmd等)`python main.py`と入力する
するとファイルの名前がずらずらと出ますが、これで正常に動いています。
しばらく待つと画像ファイルにそれぞれタグが記載されたtxtファイルが出力されます。

- どのJSONファイルからtxtファイルを作ったかを記録したJSONファイルが出力されます。それが嫌な場合はconfig.iniで`RecordConverted = False` そうでない場合は `RecordConverted = True`としてください。
- もしスクリプトが動かなかったり、苦情、提案などあればご連絡ください。
