# soyosan_seodongtan


- 공유 풀려있는 경우
  - 공유를 다시 걸어줘라

- ip주소가 v6로 나오는 겅유
    ```
    ping -4 raspberrypi.local
    ```

- Adafruit_Python_PCA9685
- Adafruit-Motor-HAT-Python-Library
- Adafruit_Python_SSD1306
- Raspi-MotorHAT-python3.zip / Raspi-MotorHAT-python3

- 봉쥬르 설치
  - https://support.apple.com/kb/DL999?locale=en_US&viewlocale=ko_KR
- 봉쥬르 라즈찾기 명령어  
```
dns-sd -G v4 raspberrypi.local
```
- 내꺼는
```
dns-sd -G v4 pidh.local
```
- 라즈베리파이 무선은 뭘 해도 안된다..
- 그냥 ssh 연결..
```
ssh pi@pidh.local
```



# 4
## SAMBA(옵션..)
- 삼바 설치
```
sudo apt-get install -y samba samba-common-bin
```


- 삼바 계정과 패스워드 설정
```
sudo smbpasswd -a pi
```
패스워드는 raspberry

- 삼바 설정파일 변경을 위해
```
sudo nano /etc/samba/smb.conf
```

- 맨 아랫줄에 추가해줘야하는거
```
[pi]
comment = rpi samba server by girin
path = /home/pi
valid user = pi
writable = yes
read only = no
browseable = yes
```


- 삼바 재시작
```
sudo service smbd restart
```
- 아래 두개는 안되는거 (과거의 버전 혹은 데비안 배포판에 따라 다름..
```
sudo service samba restart
sudo /etc/init.d/samba restart
```

- 참고 링크 : https://fishpoint.tistory.com/1553

