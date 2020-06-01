import Tkinter as tk
import os

def manual():
    os.system("python manualmotor.py")

def auto():
    os.system("python autonomousnew.py")

def stop():
    os.system("python stopall.py")

def reb():
    os.system("sudo reboot")

def shu():
    os.system("sudo shutdown -h now")

def lidar():
    os.system("python /home/pi/BreezySLAM-master/examples/xvslam.py &")

def thermal():
    os.system("python Adafruit_AMG88xx_python_examples/thermal_cam.py &")

def camera():
    os.system("sudo python /home/pi/Desktop/SeniorDesign/camerastream.py &")

command = tk.Tk()
frame = tk.Frame(command)
frame.pack()
button6 = tk.Button(frame,
                   text="SLAM Lidar",
                   command=lidar)
button6.grid(row=4, column=2)
button7 = tk.Button(frame,
                   text="Thermal View",
                   command=thermal)
button7.grid(row=8, column=2)
button8 = tk.Button(frame,
                   text="Camera View",
                   command=camera)
button8.grid(row=12, column=2)
button = tk.Button(frame,
                   text="Manual Mode",
                   command=manual)
button.grid(row=16, column=2)
button2 = tk.Button(frame,
                   text="Autonomous Mode",
                   command=auto)
button2.grid(row=20, column=2)
button3 = tk.Button(frame,
                   text="Force Stop",
                   command=stop)
button3.grid(row=24, column=2)
button4 = tk.Button(frame,
                   text="Reboot Robot",
                   command=reb)
button4.grid(row=28, column=2)
button5 = tk.Button(frame,
                   text="Shutdown Robot",
                   command=shu)
button5.grid(row=32, column=2)
command.geometry('+%d+%d' % (1600,600))
command.title('Select Mode')
command.mainloop()
