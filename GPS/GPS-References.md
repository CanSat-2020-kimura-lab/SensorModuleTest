## プログラム概要
### GPS-test.py 
・GPSのBBM用テストプログラム (没)

### GPS-Navigate.py
・GPSによるローバー制御プログラム

### microGPS-deetail.md
・microGPSライブラリの仕様書 (没)

### softSerialTest.py
・GPSのBBM用テストプログラム(2019と同じ)

***
## ライブラリの概要と主要な構文
・[serial](https://qiita.com/kosystem/items/0023cfee941fdf099087) : シリアル通信を可能にする<br>
⇒ .serial.Serial('<シリアルポート名>',<ボーレート>,timeout=<数>)<br>
⇒ .read() : ()の中の数の分読み込む<br>
⇒ .readline() : 行末端まで読み込む<br>
⇒ .decode('utf-8') : 受信したものをutf-8の文字列に変換<br>

・[micropyGPS](https://github.com/inmcm/micropyGPS) : GPSモジュールから送られてくるデータ(NMEA-0183というフォーマットの文字列)を扱う<br>
⇒ **使うためにはGithubからmicropyGPS.pyをダウンロードして、Pythonを起動するディレクトリーに置く**<br>
⇒詳細は[こちら](https://github.com/CanSat-2020-kimura-lab/SensorModuleTest/blob/master/GPS/microGPS-detail.md)

・[threading](https://docs.python.org/ja/3/library/threading.html) : 並列処理をする<br>
⇒ .start() : スレッドの活動を開始する。スレッドオブジェクト１つに対して、１回しか使えない<br>
⇒ .daemon : このスレッドがデーモンスレッドか (True) か否か (False) を示すブール値。必ずstart()の前に設定する。<br>
⇒ class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

・[time](https://docs.python.org/ja/3/library/time.html?highlight=time#module-time)<br>

***
## 参考文献

・[Raspberry Pi3のPythonでGPSを扱う](https://qiita.com/AmbientData/items/fff54c8ac8ec95aeeee6)

・[ラズパイでUART通信を行う](https://masaeng.hatenablog.com/entry/2019/08/25/234002)<br>

・[[Python]緯度経度から2地点間の距離と方位角を計算する](https://qiita.com/r-fuji/items/99ca549b963cedc106ab)
