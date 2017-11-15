import serial
import os

ser = serial.Serial('/dev/ttyACM0', 9600)
onOff = 1;

while 1:

    if int(ser.readline())<75:
        print("Close");
        print(ser.readline());
        if onOff == 0:
            os.system("tvservice -o");
            ser.write('1');
            onOff = 1;

    elif int(ser.readline())>=75:
        print("Far");
        print(ser.readline());
        if onOff == 1:
            os.system("tvservice -p");
            os.system("xset -display :0 dpms force on");
            ser.write('0');
            onOff = 0;
    else:
        pass;
