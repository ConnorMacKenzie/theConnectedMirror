import json, socket, time, sys, GUIClient, speechMain 
from multiprocessing import Process
import serial


class MainClient():

    ser = serial.Serial('/dev/ttyACM0', 9600)
<<<<<<< HEAD
    onOff = 1;


    while 1:
        if int(ser.readline())<75:
            if onOff == 0:
                os.system("tvservice -p");
                os.system("xset -display :0 dpms force on");
                ser.write('1');
                onOff = 1;

        elif int(ser.readline())>=75:
            if onOff == 1:
                os.system("tvservice -o");
                ser.write('0');
                onOff = 0;
        else:
            pass;

=======
    print ser.readline()
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

        
Process(target= GUIClient.GUI()).start()
while 1:       
        Process(target= MainClient()).start()
>>>>>>> 49685d49eb587cac01385979a47d2ec7028fb4ff
        
main = MainClient()   

    

