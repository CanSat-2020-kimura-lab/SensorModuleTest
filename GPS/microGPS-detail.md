# micropyGPS

## はじめに
以下の文章は<https://github.com/inmcm/micropyGPS>をgoogle翻訳にかけた結果をコピーしたものです

## 概観
micropyGPSは、MicroPythonおよびPyBoard組み込みプラットフォームで使用するためのフル機能のGPS NMEA文パーサーです。また、Python 3.xと完全に互換性があります。

## 特徴
重要なNMEA-0183出力メッセージのほとんどを解析して検証し、扱いやすいデータ構造にします
GPSデータを解釈、表示、記録、および操作するヘルパーメソッドを提供します
Micropythonで利用可能な標準ライブラリのみを使用して、純粋なPython 3.xで記述
組み込みプロジェクトに簡単に統合できるように、単一ファイル内の単一クラスとして実装されます
シリアルUARTデータソースを考慮して記述されたパーサー。ノイズの多い組み込み環境向けの堅牢なエラー処理により、一度に1つの文字で動作します
偉大なTinyGPS Arduinoライブラリをモデルにしています

## インストール/アンインストール
gitからクローンを作成し、setuptoolsを介してインストールを実行してインストールします。
<pre>
  git clone https://github.com/inmcm/micropyGPS.git
  python setup.py install
</pre>
または、pipを使用してgithubから直接インストールします。
<pre>
pip install git + https：//github.com/inmcm/micropyGPS.git
</pre>
アンインストールするには、次のpipコマンドを使用します。
<pre>
pip uninstall micropyGPS
</pre>

## 基本的な使い方

micropyGPSは使いやすいです。micropyGPS.pyをプロジェクトディレクトリにコピーし、MicropyGPSクラスをスクリプトにインポートします。そこから、新しいGPSオブジェクトを作成し、update（）メソッドを使用してデータのフィードを開始します。有効な文全体をフィードすると、文のタイプが返され、内部GPS属性が更新されます。以下の例は、RMC文の構文解析を示しており、オブジェクトは現在の緯度データを含むタプルを返します

<pre>
>>> from micropyGPS import MicropyGPS
>>> my_gps = MicropyGPS()
>>> my_sentence = '$GPRMC,081836,A,3751.65,S,14507.36,E,000.0,360.0,130998,011.3,E*62'
>>> for x in my_sentence:
...     my_gps.update(x)
...
'GPRMC'
>>> my_gps.latitude
(37, 51.65, 'S')
</pre>

オブジェクトは、存在する限り、新しい文字を受け入れ、文を解析し続けます。構文解析される各タイプの文は、GPSオブジェクトのさまざまな内部属性を更新できます。

pytestがインストールされている場合、test_micropyGPS.pyスクリプトを使用して実行すると、さまざまなタイプの多数の例文が解析され、さまざまな解析、ロギング、印刷の仕組みがテストされます。
<pre>
$ pytest -svvv test_micropyGPS.py
</pre>
現在サポートされている文
<pre>
    GPRMC
    GLRMC
    GNRMC
    GPGLL
    GLGLL
    GNGLL
    GPGGA
    GLGGA
    GNGGA
    GPVTG
    GLVTG
    GNVTG
    GPGSA
    GLGSA
    GNGSA
    GPGSV
    GLGSV
</pre>

## 位置データ

有効な文から正常に解析されたデータは、簡単にアクセスできるオブジェクト変数に格納されます。複数のコンポーネント（緯度と経度など）を含むデータはタプルに格納されます。

<pre>
##緯度は37°51.65 'S
>>> my_gps.latitude
（37、51.65、 'S'）
＃経度は145°7.36 'E
>>> my_gps.longitude
（145、7.36、「E」）
＃コースは54.7°
>>> my_gps.course
54.7
＃高度は280.2メートル
>>> my_gps.altitude
280.2
＃理想的なジオイドからの距離は-34メートル
>>> my_gps.geoid_height
-34.0
</pre>
現在の速度は、ノット、マイル/時、キロメートル/時を表す値のタプルに保存されます
<pre>
>>> my_gps.speed
（5.5、6.3305、10.186）
</pre>

## 日付と時刻

現在のUTC時刻が格納されます（時間、分、秒）
<pre>
>>> my_gps.timestamp
（8、18、36.0）
>>> my_gps.date
（22、9、05）
</pre>
タイムゾーンは、オブジェクトの作成時またはその後いつでもlocal_offsetを設定することにより、を使用するように自動的に調整できます。 -5に設定すると、米国の東部標準時になります。
<pre>
>>> my_gps = MicropyGPS（-5）
>>> my_gps.local_offset
-5
＃タイムスタンプ文データで更新...
>>> my_gps.timestamp
（3、18、36.0）
</pre>
現在のUTC日付が保存されます（日、月、年）。注：現在、日付はlocal_offsetで設定されたタイムゾーンと一致するように調整されていません。
<pre>
>>> my_gps.date
（22、9、05）
</pre>

## 衛星データ

信号品質と個々の衛星情報は、GSV、GSA、およびGGAセンテンスから収集され、次の変数で利用可能になります。
<pre>
>>> my_gps.satellites_in_use
7
>>> my_gps.satellites_used
[7、2、26、27、9、4、15]
＃修正タイプは次のとおりです。1=修正なし、2 = 2D修正、3 = 3D修正
>>> my_gps.fix_type
３
＃1.0に近い希釈率（DOP）の値は、優れた品質の位置データを示します
>>> my_gps.hdop
1.0
>>> my_gps.vdop
1.5
>>> my_gps.pdop
1.8
</pre>
個々の衛星データを読み取る前に、satellite_data_updated（）メソッドがTrueであることを確認する必要があります。これにより、関連するすべてのGSV文が解析され、衛星情報が完全になります
<pre>
>>> my_gps.satellite_data_updated（）
True
＃衛星データは、キーが衛星番号で値ペアが（標高、方位角、SNR（利用可能な場合））を含むタプルである辞書です。
>>> my_gps.satellite_data
{19：（5、273、なし）、32：（5、303、なし）、4：（22、312、26）、11：（9、315、16）、12：（19、88、23） 、14：（64、296、22）、15：（2、73、なし）、18：（54、114、21）、51：（40、212、なし）、21：（16、175、なし） 、22：（81、349、25）、24：（30、47、22）、25：（17、127、18）、31：（22、204、なし）}
＃可視の衛星PRNのみを返します
>>> my_gps.satellites_visible（）
[19、32、4、11、12、14、15、18、51、21、22、24、25、31]
</pre>

## GPS統計

文章を解析している間、MicropyGPSオブジェクトは解析された文章の数とCRC失敗の数を追跡します。 parsed_sentencesは、基本センテンスキャッチャーを通過したクリーンなCRCを持つセンテンスです。 clean_sentencesは、特定の関数によって正常に解析された文の数を示します。
<pre>
>>> my_gps.parsed_sentences
14
>>> my_gps.clean_sentences
14
>>> my_gps.crc_fails
0
</pre>

有効な修正データを含む最後の文が解析されてから経過したリアルタイムの時間も利用可能になります。注：pyBoardではこの値はミリ秒単位で返され、Unix / Windowsではこの値は秒単位で返されます。
<pre>
＃pyBoardでの実行を想定
>>> my_gps.time_since_fix（）
3456
</pre>
ロギング

micropyGPSは現在、生のNMEAセンテンスデータの非常に基本的な自動ロギングをファイルに実行できます。ロギングが有効になっているときにパーサーに渡された有効なASCII文字は、ターゲットファイルに記録されます。これは、GPS文を処理する場合に役立ちますが、収集したデータをアーカイブまたはさらに分析するために保存する必要があります。ログファイルの相対的なサイズのため、STM32マイクロのエミュレートされたメモリではなく、SDカードをストレージメディアとして使用することを強くお勧めします。操作が成功したかどうかにかかわらず、すべてのロギングメソッドはブール値を返します。
<pre>
＃ロギングはstart_logging（）でいつでも開始できます
>>> my_gps.start_logging（ 'log.txt'）
True
＃任意の文字列をwrite_log（）メソッドでログファイルに書き込むことができます
>>> my_gps.write_log（ 'ログファイルに関する注意事項'）
True
＃ロギングを停止し、stop_logging（）でログファイルを閉じます
>>> my_gps.stop_logging（）
True
</pre>

## きれいな印刷

GPSデータをタプルや整数よりも優れた形式で表現できるようにするいくつかの関数が含まれています。
<pre>
>>> my_gps.latitude_string()
"41° 24.8963' N"
>>> my_gps.longitude_string()
"81° 51.6838' W"
>>> my_gps.speed_string('kph')
'10.186 km/h'
>>> my_gps.speed_string('mph')
'6.3305 mph'
my_gps.speed_string('knot')
'5.5 knots'
＃現在のコースに基づく最も近いコンパスポイント
my_gps.compass_direction()
'NE'
>>> my_gps.date_string('long')
'September 13th, 2098'
＃1900年代に取得したGPSデータには正しい世紀を指定する必要があることに注意してください
>>> my_gps.date_string('long','19')
'September 13th, 1998'
>>> my_gps.date_string('s_mdy')
'09/13/98'
>>> my_gps.date_string('s_dmy')
'13/09/98'
</pre>

## Pyboardの使用
pyboardプラットフォームでmicropyGPSを使い始めるのに役立つテストスクリプトが含まれています。これらのスクリプトは、pyboardsの内部メモリにコピーするか、SDカードに配置できます。 pyboardでスクリプトを実行するときに、使用しているスクリプトの名前をmain.pyに変更するか、実行するスクリプトの名前でboot.pyを更新してください。

・**uart_test.py**は、GPSが接続されており、UARTが正しく構成されているかどうかをテストする単純なUARTエコープログラムです。すべて正常である場合、標準のNMEAセンテンスの一部は1秒に1回（またはGPS更新レートに応じてより速く）印刷する<br>
・**statement_test.py**は、UARTからのすべての着信文字を試行して解析します。このスクリプトでは、micropyGPS.pyが同じストレージ領域（SDカードまたは内部）に存在する必要があります。有効な文を構成する文字のセットが受信されて解析されるたびに、スクリプトは文のタイプを出力します。<br>
・**GPIO_interrupt_updater.py**は、外部割り込みを使用してGPSデータの更新をトリガーする方法の例です。この場合、周期的な信号（1Hz GPS出力）がピンX8に接続され、毎秒質量分析イベントが発生します。<br>

受信機のボーレートと更新レートの調整は、付属のMTK_commandスクリプトで簡単に実行できます。

pyboardをAdafruit Ultimate GPS Breakoutに接続する方法の例（外部割り込みの例で必要なPPS信号を除く）を以下に示します。

## ESP32

pyboardのセットアップ手順に従うことができます。唯一の違いは、micropyGPSをフリーズしたモジュールとして使用することです。それ以外の場合は、利用可能なヒープ領域が不足しているため、例外が発生します。

## その他のプラットフォーム

上記のように、micropyGPSはPython3.xでも動作します（開発の大部分はここで行われます！）。これは、コードのテストや、既存のログファイルの解析に役立ちます。

pyBoardとESP32を超えて、micropyGPSは、Raspberry PiやBeagleBoneボードなどのPython3インタープリターを備えた他の組み込みプラットフォームで実行する必要があります。これらの他のデバイスは現在テストされていません。
