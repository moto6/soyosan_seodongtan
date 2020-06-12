from Raspi_MotorHAT import Raspi_MotorHAT
import time

servoMin= 70
servoMax= 120

mh = Raspi_MotorHAT(0x6F) # motor-HAT i2c주소

myMotor = mh.getMotor(3)
myMotor.setSpeed(150)
#myMotor.run()
myMotor.run(Raspi_MotorHAT.FORWARD)




servo = mh._pwm
# pwm frequency 설정하기 서보컨트롤에서는 50Hz 혹은 60Hz가 일반적이다. (여기에서는 60Hz 사용.)
servo.setPWMFreq(60)
while(True):
	servo.setPWM(0, 4096, 0)
	time.sleep(1)
	servo.setPWM(0, 0, 4096)
	time.sleep(1)

