#import serial
import os
import serialversion2


def test_lcdlow():
    
    test = serialversion2.lcd_control()
    onoff = test.lcdon(4)
    if onoff != 0:
        raise AssertionError()
    else:
        print("passes test")

def test_lcdright():
    test = serialversion2.lcd_control()
    onoff = test.lcdon(10)
    if onoff != 1:
        raise AssertionError()
    else:
        print("passes test")

def test_lcdhigh():
    test = serialversion2.lcd_control()
    onoff = test.lcdon(80)
    if onoff != 0:
        raise AssertionError()
    else:
        print("passes test")



        

def test_lcdbothgood():
    test = serialversion2.lcd_control()
    onoff = test.lcdoff(10,40)
    if onoff != 1:
        raise AssertionError()
    else:
        print("passes test")

def test_lcdtimerbad():
    test = serialversion2.lcd_control()
    onoff = test.lcdoff(10,10)
    if onoff != 0:
        raise AssertionError()
    else:
        print("passes test")
        
def test_lcddistancelow():
    test = serialversion2.lcd_control()
    onoff = test.lcdoff(3,40)
    if onoff != 0:
        raise AssertionError()
    else:
        print("passes test")

def test_lcddistancehigh():
    test = serialversion2.lcd_control()
    onoff = test.lcdoff(80,40)
    if onoff != 0:
        raise AssertionError()
    else:
        print("passes test")

def test_lcdbothbad():
    test = serialversion2.lcd_control()
    onoff = test.lcdoff(4,10)
    if onoff != 0:
        raise AssertionError()
    else:
        print("passes test")
