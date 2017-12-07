import serial
import os

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1:

    if int(ser.readline())<75:
        print("Close");
        print(ser.readline());

    elif int(ser.readline())>=75:
        print("Far");
        print(ser.readline());
        
    else:
        pass;
