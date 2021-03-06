import pigpio
import time

Ena1 = 12
Pha1 = 21
LARGE = 8
MODE = 7
STBY = 18

pi1 = pigpio.pi()
pi1.set_mode(Ena1, pigpio.OUTPUT)
pi1.set_mode(Pha1,pigpio.OUTPUT)
pi1.set_mode(MODE,pigpio.OUTPUT)
pi1.set_mode(LARGE,pigpio.OUTPUT)
pi1.set_mode(STBY,pigpio.OUTPUT)

def set_motor(pi1, a, b, t):
	pi1.write(Ena1, a)
	pi1.write(Pha1,b)
	time.sleep(t)

def set_const(pi1,c, d, e, t):
	pi1.write(MODE,c)
	pi1.write(LARGE,d)
	pi1.write(STBY,e)
	time.sleep(t)

try:
	set_motor(pi1, 0, 0, 2.0) # stop (neutral)
	set_const(pi1,1, 0, 1, 0.3)
	for i in range(2):
		set_motor(pi1, 1, 1, 2.0) # normal rotation
		set_motor(pi1, 0, 0, 1.0) # brake


	for i in range(2):
		set_motor(pi1, 1, 0, 2.0) # reverse rotation
		set_motor(pi1, 0, 0, 1.0) # brake

except KeyboardInterrupt:
	print ("done!")
	set_moter(pi1,0, 0, 0.5)

set_motor(pi1, 0, 0, 0.5) # stop (neutral)
pi1.set_mode(Ena1, pigpio.INPUT)
pi1.set_mode(Pha1,pigpio.INPUT)
pi1.stop()
