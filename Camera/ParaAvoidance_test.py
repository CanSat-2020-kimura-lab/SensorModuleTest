import sys
sys.path.append('/home/pi/git/kimuralab/SensorModuleTest/Camera')
sys.path.append('/home/pi/git/kimuralab/Detection')
sys.path.append('/home/pi/git/kimuralab/SensorModuleTest/TSL2561')
import time
import difflib
import pigpio
import serial
import binascii
import Capture
import ParaDetection
import runtest
import TSL2561
import cv2
import numpy as np

def ParaJudge():
	t1 = time.time()
	t2 = t1
	while(t2 - t1 <= 60):
		lux=TSL2561.readLux()
		print("lux1: "+str(lux[0]))

		if lux[0]<100:
			time.sleep(5)
			t2 = time.time()
		else:
			break

def ParaAvoidance():
	n = 0
	#GPS.openGPS()
	#GPS_init = GPS.readGPS()
	#GPS.closeGPS()

	#GPS_now = GPS_init
	dist = 0
	try:
		while dist <= 0.020 :
			Capture.Capture(n)
			img = cv2.imread('photo/photo' + n + '.jpg')
			flug = ParaDetection.ParaDetection(img)
			if flug == 0:
				Motor.run = Run()
				Motor.run.straight()
				#GPS_now = GPS.readGPS()
				#dist = Cal_rho(GPS_now[2], GPS_now[1], GPS_init[2], GPS_init[1])
				Motor.run.stop()
				dist += 0.02

			else:
				Motor.run = Run()
				Motor.run.back
				Motor.run.stop()

	except KeyboardInterrupt:
		Motor.run.stop()
	
	#GPS.closeGPS()

if __name__ == '__main__':
	print("ParaJudge start")
	ParaJudge()
	print("ParaAvoidance start")
	ParaAvoidance()
