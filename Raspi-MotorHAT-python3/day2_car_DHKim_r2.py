# day2_car.py
# input()으로 명령. 모터 테스트

from Raspi_MotorHAT import Raspi_MotorHAT#, Raspi_DCMotor

# 모터 설정
mh = Raspi_MotorHAT(addr=0x6f)
dcMotor = mh.getMotor(3)    # M3단자에 모터 연결
speed = 125 # 기본 속도 0~255
dcMotor.setSpeed(speed)
# 서보 설정
servo = mh._pwm
servo.setPWMFreq(60)

#여기를 바꾸어서 자신의 서보모터에 맞게 설정해주세요
R_limit = 450
L_limit = 250
mid_center = 350


# 각도 환산 알고리즘
L_itv = L_limit-mid_center
R_itv = R_limit-mid_center

# 앞으로
def go():
    dcMotor.run(Raspi_MotorHAT.FORWARD)

# 뒤로
def back():
    dcMotor.run(Raspi_MotorHAT.BACKWARD)

# 모터 작동 중지
def stop():
    dcMotor.run(Raspi_MotorHAT.RELEASE)

# 빠르게
def speedUp():
    global speed
    speed = 255 if speed >= 235 else speed+20 #최대255, 20단위로 증감
    dcMotor.setSpeed(speed)

# 느리게
def speedDown():
    global speed
    speed=0 if speed <= 20  else speed-20  # 최하 0
    dcMotor.setSpeed(speed)

# 각도만큼 핸들 틀기
def steer(angle=0): # 각도 +30˚~ -30˚
    if angle <= -30: # 서보의 작동범위는 좌우 양 극단의 30˚까지는 가지 않는다.
        angle = -30

    if angle >= 30:
        angle = 30
    #pulse_time = 200+(614-200)//180*(angle+90)  # 200:-90˚ ~ 614:+90˚ 비율에 따라 맵핑
    pulse_time = mid_center

    if angle == 0 :
        pulse_time = mid_center
        servo.setPWM(0,0,mid_center)

    elif angle > 0 : # LEFT
        #a2pul = int(angle*L_itv/30) + mid_center
        pulse_time = int(angle*L_itv/30) + mid_center
        servo.setPWM(0,0,pulse_time)

    elif angle < 0 : #RIGHT
        pulse_time = int(angle*R_itv/30)*(-1) + mid_center
        servo.setPWM(0,0,pulse_time)
        
    else :
        servo.setPWM(0,0,pulse_time)
    #pulse_time = 170+(340-200)//180*(angle+90) 
    #servo.setPWM(0,0,pulse_time)

# 우회전
def steer_right():
    steer(30)

# 좌회전
def steer_left():
    steer(-30)

# 핸들 중앙
def steer_center():
    steer(0)

def main():
    command = ['앞으로', '뒤로', '정지', '빠르게', '느리게', '오른쪽', '왼쪽', '중앙']
    func = [go, back, stop, speedUp, speedDown, steer_right, steer_left, steer_center]
 
    try:
        while True:
            word = input("명령['앞으로', '뒤로', '정지', '빠르게', '느리게', '오른쪽', '왼쪽', '중앙']: ")
            if word in command:
                func[command.index(word)] ()  # word에 해당하는 index의 func 
                
    except KeyboardInterrupt:
        print("\n사용자의 요청으로 종료합니다..")
    except:
        print("\n알 수 없는 오류입니다.")
    finally:    # 종료할 때는 모든 모터 멈추기
        mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
        mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
        mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
        mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

if __name__ == "__main__":
    main()
