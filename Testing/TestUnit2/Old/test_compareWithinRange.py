import serial
import os
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

os.system("tvservice -o")
onOff = 0;
time.sleep(5);

while 1:

    if int(ser.readline())<75:
        print("Close");
        print(ser.readline());
        if(onOff==0):
            os.system("tvservice -p");
	    os.system("xset -display :0 dpms force on");
	    onOff=1;
