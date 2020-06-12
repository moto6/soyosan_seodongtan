sudo apt-get update
sudo apt-get install libjpeg-dev -y
sudo apt-get install zlib1g-dev -y
sudo apt-get install libfreetype6-dev -y
sudo apt-get install liblcms1-dev -y
sudo apt-get install libopenjp2-7 -y
sudo apt-get install libtiff5 -y
pip3 install pillow
pip3 install Adafruit-SSD1306
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
sudo apt-get install python-smbus i2c-tools
sudo i2cdetect -y 1
wget http://raspberrypiwiki.com/images/a/ac/Raspi-MotorHAT-python3.zip
unzip Raspi-MotorHAT-python3.zip

