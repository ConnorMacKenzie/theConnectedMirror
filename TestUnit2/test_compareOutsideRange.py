import serial
import os

ser = serial.Serial('/dev/ttyACM0', 9600)
onOff = 1;
os.system("tvservice -p");
os.system("xset -display :0 dpms force on");

while 1:

    if int(ser.readline())>=75:
        print("Far");
        print(ser.readline());
        if onOff == 1:
            os.system("tvservice -o");
            onOff = 0;

    else:
        pass;
