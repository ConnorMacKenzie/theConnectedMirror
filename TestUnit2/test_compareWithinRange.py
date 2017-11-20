import serial
import os

ser = serial.Serial('/dev/ttyACM0', 9600)

os.system("tvservice -o")
onOff = 0;

while 1:

    if int(ser.readline())<75:
        print("Close");
        print(ser.readline());
        if(onOff==0):
            os.system("tvservice -p");
            os.system("xset -display :0 dpms force on");

    else:

        pass;
