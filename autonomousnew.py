from distancer import get_distancer
from distancel import get_distancel
from distancef import get_distancef
from Adafruit_AMG88xx import Adafruit_AMG88xx
import RPi.GPIO as gpio
import time
import random
import os

gpio.setwarnings(False)

r_motor1=33
r_motor2=17
l_motor1=10
l_motor2=9
sensor = Adafruit_AMG88xx()
time.sleep(0.1)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(r_motor1, gpio.OUT)
    gpio.setup(r_motor2, gpio.OUT)
    gpio.setup(l_motor1, gpio.OUT)
    gpio.setup(l_motor2, gpio.OUT)

def forward():
    init()
    gpio.output(r_motor1, False)
    gpio.output(r_motor2, True)
    gpio.output(l_motor1, False)
    gpio.output(l_motor2, True)
    gpio.cleanup()

def reverse(lol):
    init()
    gpio.output(r_motor1, True)
    gpio.output(r_motor2, False)
    gpio.output(l_motor1, True)
    gpio.output(l_motor2, False)
    time.sleep(lol)
    gpio.cleanup()

def left(lol):
    init()
    gpio.output(l_motor1, False)
    gpio.output(l_motor2, True)
    gpio.output(r_motor1, True)
    gpio.output(r_motor2, False)
    time.sleep(lol)
    gpio.cleanup()

def right(lol):
    init()
    gpio.output(l_motor2, False)
    gpio.output(l_motor1, True)
    gpio.output(r_motor2, True)
    gpio.output(r_motor1, False)
    time.sleep(lol)
    gpio.cleanup()

def stop():
    init()
    gpio.output(r_motor2, False)
    gpio.output(r_motor1, False)
    gpio.output(l_motor2, False)
    gpio.output(l_motor1, False)
    gpio.cleanup()

def checkfront():
    global thisisfrontsensor
    global thisisrightsensor
    global thisisleftsensor
    global pix
    init()

    thisisfrontsensor=get_distancef()
    thisisrightsensor=get_distancer()
    thisisleftsensor=get_distancel()

    pix=sensor.readPixels()
    pixloc=[]
    ## if statement to calculate location of the heat source in thermal camera
    for i in (i for i, x in enumerate(pix) if x > 28):
            pixloc.append(i+1)
    pixleft=[x for x in pixloc if x <= 20]
    pixright=[x for x in pixloc if x >= 44]
    print"\nMax temp ",max(pix)," celsius"
    ## robot movement algorithm
    if len(pixleft) > len(pixright) and max(pix) < 30:
        print "RIGHT towards heat source"
        right(2)
    elif len(pixright) > len(pixleft) and max(pix) < 30:
        print "LEFT towards heat source"
        left(2)
    elif len(pixright) == len(pixleft) and max(pix) < 30:
        if thisisfrontsensor < 50 or thisisrightsensor < 50 or thisisleftsensor < 50:

            if thisisfrontsensor <50:
                print "STOP & reverse. Front sensor >", round(thisisfrontsensor),"cm.Right sensor :",round(thisisrightsensor),"cm. Left sensor :",round(thisisleftsensor),"cm"
                stop()
                time.sleep(1.5)
                reverse(1)
                ## if statement to randomize reverse direction
                if bool(random.getrandbits(1)):
                    right(1)
                else:
                    left(1)
            elif thisisrightsensor - thisisleftsensor > 0 :
                print "RIGHT. Front sensor >", round(thisisfrontsensor),"cm.Right sensor :",round(thisisrightsensor),"cm. Left sensor :",round(thisisleftsensor),"cm"
                right((thisisrightsensor - thisisleftsensor)/100)
                stop()
            else:
                print "LEFT. Front sensor >", round(thisisfrontsensor),"cm.Right sensor :",round(thisisrightsensor),"cm. Left sensor :",round(thisisleftsensor),"cm"
                left((thisisleftsensor-thisisrightsensor)/100)
                stop()
        else:
            print "FORWARD. Front sensor >", round(thisisfrontsensor),"cm.Right sensor :",round(thisisrightsensor),"cm. Left sensor :",round(thisisleftsensor),"cm"
            forward()

while True:
    checkfront()
    ## if statment to break while loop
    if max(pix) >= 30:
        print"\n!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!VICTIMS FOUND!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!\nStopping Autonomouse Mode\n"
        os.system("python stopall.py")
        break
