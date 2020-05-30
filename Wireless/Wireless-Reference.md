## プログラム概要
### Wireless-test.py
・通信モジュールのBBM用テストプログラム<br>
・参考文献をコピーしたものだが、そのままでは使えない気がしたため去年のも置いておく

### Wireless-test2.py
・通信モジュールのBBM用テストプログラム<br>
・去年と同じ

### IM920.py
・IM920ライブラリ

***
## ライブラリの概要と主要な構文
※同じライブラリでもリンク先が違うことがあるため注意
### IM920.py
・[serial](https://pyserial.readthedocs.io/en/latest/pyserial_api.html)<br>

### Wireless-test2.py
・[sys](https://qiita.com/jp0003menegi/items/fbf407af7d294c09481a) : Pythonのインタプリタや実行環境に関する情報を扱うためのライブラリ<br>

・[time](https://docs.python.org/ja/3/library/time.html?highlight=time#module-time)<br>

・[difflib](http://docs.daemon.ac/python/Python-Docs-2.5/lib/module-difflib.html) : 差異の計算を助ける<br>

・[pigpio](http://abyz.me.uk/rpi/pigpio/python.html) : GPIOを制御する<br>
⇒ .pigpio.py : 必須。<br>
⇒ .set_mode() : GPIOモードを設定<br>
⇒ .write : GPIOを書き込む<br>

・[serial](https://qiita.com/kosystem/items/0023cfee941fdf099087)　: シリアル通信を可能にする<br>

・[binascii](https://docs.python.org/ja/3/library/binascii.html) : バイナリデータと ASCII データとの間での変換<br>

・IM920 : 自作関数

・convertIMG2BYTES : 自作関数と思われる。文字列とバイト列の変換

・[cv2](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_image_display/py_image_display.html) : 画像を扱う<br>
⇒cv2.imread_color : カラー画像として読み込む．画像の透明度は無視される．デフォルト値<br>
⇒cv2.imread_grayscale : グレースケール画像として読み込む<br>
⇒cv2.imread_unchanged : アルファチャンネルも含めた画像として読み込む<br>
⇒cv2.imshow() : 画像を表示する<br>
⇒cv2.imwrite() : 画像を保存する<br>


### Wireless-test.py
・[serial](https://qiita.com/kosystem/items/0023cfee941fdf099087)　: シリアル通信を可能にする<br>

・[binascii](https://docs.python.org/ja/3/library/binascii.html) : バイナリデータと ASCII データとの間での変換<br>

・[signal]()<br>

・[sys](https://qiita.com/jp0003menegi/items/fbf407af7d294c09481a) : Pythonのインタプリタや実行環境に関する情報を扱うためのライブラリ<br>

・[platform](https://docs.python.org/ja/3/library/platform.html) : 実行中プラットフォームの固有情報を参照する<br>
⇒ .system() : OS名を返す

from serial.tools import list_ports

***
## 参考文献

・[IM920を簡単に使えるモジュールを作ってみた](https://www.autumn-color.com/archives/298)<br>
・[IM920を簡単に使えるモジュールを作ってみた(GitHub)](https://github.com/Momijinn/IM920MHz_Module)
