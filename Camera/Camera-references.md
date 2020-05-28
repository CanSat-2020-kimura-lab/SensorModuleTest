## プログラム説明
## camera-test.py
・概要：カメラモジュールのBBM用プログラム<br>

## モジュールの概要と主要な構文
・[time]()<br>
・[picamera](http://igarashi-systems.com/sample/translation/raspberry-pi/usage/python-camera.html)<br>
⇒ import picamera : ライブラリを利用可能にする<br>
⇒ camera = picamera.PiCamera() : インスタンス作成<br>
⇒ camera.capture : 写真を撮る<br>
⇒ camera.start_preview() : スクリーンにカメラフィードのプレビューを表示する<br>
⇒ sleep(5) : 5秒スリープ(timeモジュールをインポートすることで利用可能)<br>

## 参考文献

・[Raspberry pi とカメラモジュールを使った画像保存(とおまけに動画)](https://qiita.com/Ponjiro/items/ab3700394faab7422bb3)
