# --- IM920 debugging program --- #
import sys
sys.path.append('/home/pi/git/kimuralab/SensorModuleTest/Wireless')
sys.path.append('/home/pi/git/kimuralab/SensorModuleTest/GPS')

import serial
import binascii
import signal
import platform
import pigpio
from time import sleep

portnumber = '/dev/ttyAMA0'

import IM920
import GPS

pi = pigpio.pi()

if __name__ == '__main__':
	try:
		GPS.openGPS()
		pi = pigpio.pi()
		pi.set_mode(22,pigpio.OUTPUT)
		print('IM920 poweron')
		pi.write(22,1)
		print('Send Start')
		while 1:
			gpsdata = GPS.readGPS()
			#IM920.Srid(19200,'3156')       #ペアリング
			#IM920.Erid(19200)              #削除
			#IM920.Send('Hello')      #文字列送信
			IM920.Send(str(gpsdata))
			#print(IM920.Reception(19200))  #文字列受信
			#IM920.Repeater(19200)          #中継機化
			#IM920.Rdid(19200)               #固有ID
			#IM920.Stch(19200, '01')        #無線通信チャンネルの設定
			#IM920.Rdch(19200)              #無線通信チャンネルの読み出し
			#IM920.Rdrs(19200)               #RSSI値(現在の信号強度レベル)読み出し
			#IM920.Stpo(19200, '3')         #通信出力の設定
			#IM920.Rdpo(19200)               #通信出力の読み出し
			#IM920.Strt(19200, '2')         #無線通信速度の設定
			#IM920.Rdrt(19200)               #無線通信速度の読み出
			#IM920.Rprm(19200)              #パラメータ一括読み出し
			#IM920.Sbrt(19200, '4')          #ボーレート設定
			sleep(3)
	except:
		pass
	finally:
		GPS.closeGPS()
		pi.write(22,0)
		print('IM920 poweroff')
