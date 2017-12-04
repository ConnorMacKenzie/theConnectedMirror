import time, sys, os 
import serial


class MainClient():

        ser = serial.Serial('/dev/ttyACM0', 9600)

        start = 0
        end = 0
        isTimer = False
        onOff = 1;


        while 1:
                if int(ser.readline())<75:
                        if onOff == 0:
				start = time.time()
				elapsed = 0
				isTimer = False
                                os.system("tvservice -p");
                                os.system("xset -display :0 dpms force on");
                                ser.write('1');
                                onOff = 1;

                elif int(ser.readline())>=75:
                        if not isTimer:
                                start = time.time()
                                isTimer = True

                        if isTimer:
                                elapsed = time.time() - start
                                if elapsed >= 10 and onOff == 1:
                                        os.system("tvservice -o");
                                        ser.write('0');
                                        onOff = 0;
                else:
                        pass;

        
main = MainClient()   

    

