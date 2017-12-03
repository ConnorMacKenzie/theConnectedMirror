import json, socket, time, sys, speechMain, os 
from timeit import default_timer
from multiprocessing import Process
import serial
from time


class MainClient():

        ser = serial.Serial('/dev/ttyACM0', 9600)

        start = None
        end = None
        isTimer = False
        onOff = 1;


        while 1:
                if int(ser.readline())<75:
                        if onOff == 0:
                                os.system("tvservice -p");
                                os.system("xset -display :0 dpms force on");
                                ser.write('1');
                                onOff = 1;

                elif int(ser.readline())>=75:
                        if !isTimer:
                                start = time.time()
                                isTimer = True

                        if isTimer:
                                elapsed = time.time() - start
                                if elapsed >= 5 and onOff == 1:
                                        os.system("tvservice -o");
                                        ser.write('0');
                                        onOff = 0;
                                        start = None
                                        elapsed = None
                                        isTimer = False
                else:
                        pass;

                        
            
##    onOff = 1;
##
##
##
##    if int(ser.readline())<75:
##        if onOff == 0:
##            os.system("tvservice -p");
##            os.system("xset -display :0 dpms force on");
##            ser.write('1');
##            onOff = 1;
##
##    elif int(ser.readline())>=75:
##        if onOff == 1:
##            os.system("tvservice -o");
##            ser.write('0');
##            onOff = 0;
##    else:
##        pass;

        

        
main = MainClient()   

    

