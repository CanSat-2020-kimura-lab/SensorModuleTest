import pigpio
import time

AIN1 = 25
PWMA = 13

pi1 = pigpio.pi()
pi1.set_mode(AIN1, pigpio.OUTPUT)
pi1.set_mode(PWMA,pigpio.OUTPUT)

def set_motor(pi1, a, b, t):
	pi1.write(AIN1, a)
	pi1.write(PWMA,b)
	time.sleep(t)

try:
	set_motor(pi1, 0, 0, 2.0) # stop (neutral)
	for i in range(2):
		set_motor(pi1, 1, 1, 2.0) # normal rotation
		set_motor(pi1, 0, 1, 1.0) # brake


	for i in range(2):
		set_motor(pi1, 1, 0, 0.3) # reverse rotation
		set_motor(pi1, 0, 1, 1.0) # brake

except KeyboardInterrupt:
	print ("done!")

set_motor(pi1, 0, 1, 0.5) # stop (neutral)
pi1.set_mode(AIN1, pigpio.INPUT)
pi1.set_mode(PWMA,pigpio.INPUT)
pi1.stop()
