#import serial
import os



class lcd_control:

    #ser = serial.Serial('/dev/ttyACM0', 9600)
    #distance = ser.readline()

    
    @staticmethod
    def lcdon(self, distance):
        if distance >= 7 and distance <= 75:
            return 1
        else:
            return 0

    
    
            
    def lcdoff(self, distance,timer):
        if distance >= 7 and distance <= 75 and timer >= 30:
            return 1
        else:
            return 0
    
