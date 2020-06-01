import RPi.GPIO as gpio
import time
import sys
gpio.setwarnings(False)
r_motor1=17
r_motor2=22
l_motor1=10
l_motor2=9

gpio.setmode(gpio.BCM)
gpio.setup(r_motor1, gpio.OUT)
gpio.setup(r_motor2, gpio.OUT)
gpio.setup(l_motor1, gpio.OUT)
gpio.setup(l_motor2, gpio.OUT)

gpio.output(l_motor2, False)
gpio.output(l_motor1, False)
gpio.output(r_motor2, False)
gpio.output(r_motor1, False)
gpio.cleanup()