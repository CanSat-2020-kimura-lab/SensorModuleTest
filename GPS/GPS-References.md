## プログラム概要
### GPS-test.py 
・GPSのBBM用テストプログラム

***
## ライブラリの概要と主要な構文
・[serial](https://qiita.com/kosystem/items/0023cfee941fdf099087) : シリアル通信を可能にする<br>

・[micropyGPS](https://github.com/inmcm/micropyGPS) : GPSモジュールから送られてくるデータ(NMEA-0183というフォーマットの文字列)を扱う<br>
⇒ **使うためにはGithubからmicropyGPS.pyをダウンロードして、Pythonを起動するディレクトリーに置く**<br>
⇒詳細は[こちら](https://github.com/CanSat-2020-kimura-lab/SensorModuleTest/blob/master/GPS/microGPS-detail.md)

・[threading](https://docs.python.org/ja/3/library/threading.html) : 並列処理をする<br>
⇒ .start() : スレッドの活動を開始する。スレッドオブジェクト１つに対して、１回しか使えない
⇒ .daemon : このスレッドがデーモンスレッドか (True) か否か (False) を示すブール値。必ずstart()の前に設定する。

・[time](https://docs.python.org/ja/3/library/time.html?highlight=time#module-time)<br>

***
## 参考文献

・[Raspberry Pi3のPythonでGPSを扱う](https://qiita.com/AmbientData/items/fff54c8ac8ec95aeeee6)

・[[Python]緯度経度から2地点間の距離と方位角を計算する](https://qiita.com/r-fuji/items/99ca549b963cedc106ab)
