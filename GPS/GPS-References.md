## プログラム概要
### GPS-test.py 
・GPSのBBM用テストプログラム

***
## ライブラリの概要と主要な構文
・[serial](https://qiita.com/kosystem/items/0023cfee941fdf099087) : シリアル通信を可能にする<br>

・[micropyGPS](https://github.com/inmcm/micropyGPS) : GPSモジュールから送られてくるデータ(NMEA-0183というフォーマットの文字列)を扱う<br>
⇒ **使うためにはGithubからmicropyGPS.pyをダウンロードして、Pythonを起動するディレクトリーに置く**<br>

<pre>
インストール/アンインストール<br>
gitからクローンを作成し、setuptoolsを介してインストールを実行してインストールします。<br>
  git clone https://github.com/inmcm/micropyGPS.git<br>
  python setup.py install<br>
または、pipを使用してgithubから直接インストールします。<br>
  pip install git+https://github.com/inmcm/micropyGPS.git<<br>
アンインストールするには、次のpipコマンドを使用します。<br>
  pip uninstall micropyGPS<br>
</pre>

・[threading]()<br>

・[time]()<br>

***
## 参考文献

・[Raspberry Pi3のPythonでGPSを扱う](https://qiita.com/AmbientData/items/fff54c8ac8ec95aeeee6)

・[[Python]緯度経度から2地点間の距離と方位角を計算する](https://qiita.com/r-fuji/items/99ca549b963cedc106ab)
