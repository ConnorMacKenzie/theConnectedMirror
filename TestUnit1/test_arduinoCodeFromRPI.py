import serial
import os

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1:

    print(ser.readline() + "\n")
