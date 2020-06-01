import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

gpio.setwarnings(False)
##import keyboard

r_motor1=23
r_motor2=17
l_motor1=10
l_motor2=9

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(r_motor1, gpio.OUT)
    gpio.setup(r_motor2, gpio.OUT)
    gpio.setup(l_motor1, gpio.OUT)
    gpio.setup(l_motor2, gpio.OUT)


def forward1():
    init()
    gpio.output(r_motor1, False)
    gpio.output(r_motor2, True)
    gpio.output(l_motor1, False)
    gpio.output(l_motor2, True)
    time.sleep(0.1)
    gpio.cleanup()

def reverse1():
    init()
    gpio.output(r_motor1, True)
    gpio.output(r_motor2, False)
    gpio.output(l_motor1, True)
    gpio.output(l_motor2, False)
    time.sleep(0.1)
    gpio.cleanup()

def left1():
    init()
    gpio.output(l_motor1, False)
    gpio.output(l_motor2, True)
    gpio.output(r_motor1, True)
    gpio.output(r_motor2, False)
    time.sleep(0.1)
    gpio.cleanup()

def right1():
    init()
    gpio.output(l_motor2, False)
    gpio.output(l_motor1, True)
    gpio.output(r_motor2, True)
    gpio.output(r_motor1, False)
    time.sleep(0.1)
    gpio.cleanup()

def stop1():
    init()
    gpio.output(l_motor2, False)
    gpio.output(l_motor1, False)
    gpio.output(r_motor2, False)
    gpio.output(r_motor1, False)
    time.sleep(0.1)
    gpio.cleanup()


def key_input(event):
    init()
    key_press = event.char

    if key_press.lower() == 'w':
       forward1()
    elif key_press.lower() == 's':
       reverse1()
    elif key_press.lower() == 'a':
       left1()
    elif key_press.lower() == 'd':
       right1()
    else :
       pass
command = tk.Tk()
frame = tk.Frame(command)
frame.pack()
button = tk.Button(frame,
                   text="Forward",
                   repeatdelay=2,
                   repeatinterval=1,
                   command=forward1)
button.grid(row=2, column=2)
button2 = tk.Button(frame,
                   text="Left",
                    repeatdelay=2,
                    repeatinterval=1,
                   command=left1)
button2.grid(row=4, column=1)
button3 = tk.Button(frame,
                   text="Reverse",
                    repeatdelay=2,
                    repeatinterval=1,
                   command=reverse1)
button3.grid(row=4, column=2)
button4 = tk.Button(frame,
                   text="Right",
                    repeatdelay=2,
                    repeatinterval=1,
                   command=right1)
button4.grid(row=4, column=3)
print"##Robot Manual Mode##"
print"W-Forward"
print"S-Reverse"
print"D-Right"
print"A-Left"

command.bind('<KeyPress>', key_input)
command.geometry('+%d+%d' % (1600,900))
command.title('Rocker-Bogie 1.0')
command.mainloop()
