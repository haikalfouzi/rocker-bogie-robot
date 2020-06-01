import RPi.GPIO as gpio
import time
gpio.setwarnings(False)

def get_distancef ():
    gpio.setmode (gpio.BCM)
    trigf = 6
    echof = 13
    gpio.setup(trigf,gpio.OUT)
    gpio.setup(echof,gpio.IN)
    if gpio.input (echof):                                               # If the 'Echo' pin is already high
        return (100)                                                    # then exit with 100 (sensor fault)

    distancef = 0                                                        # Set initial distance to zero

    gpio.output (trigf,False)                                            # Ensure the 'Trig' pin is low for at
    time.sleep (0.05)                                                   # least 50mS (recommended re-sample time)
    gpio.output (trigf,True)                                             # Turn on the 'Trig' pin for 10uS (ish!)
    gpio.output (trigf,False)                                            # Turn off the 'Trig' pin
    time1, time2 = time.time(), time.time()                             # Set inital time values to current time

    while not gpio.input (echof):                                        # Wait for the start of the 'Echo' pulse
        time1 = time.time()                                             # Get the time the 'Echo' pin goes high
        if time1 - time2 > 0.02:                                        # If the 'Echo' pin doesn't go high after 20mS
            distancef = 100                                              # then set 'distance' to 100
            break                                                       # and break out of the loop

    if distancef == 100:                                                 # If a sensor error has occurred
        return (distancef)                                               # then exit with 100 (sensor fault)

    while gpio.input (echof):                                            # Otherwise, wait for the 'Echo' pin to go low
        time2 = time.time()                                             # Get the time the 'Echo' pin goes low
        if time2 - time1 > 0.02:                                        # If the 'Echo' pin doesn't go low after 20mS
            distancef = 100                                              # then ignore it and set 'distance' to 100
            break                                                       # and break out of the loop

    if distancef == 100:                                                 # If a sensor error has occurred
        return (distancef)                                               # then exit with 100 (sensor fault)

                                                                        # Sound travels at approximately 2.95uS per mm
                                                                        # and the reflected sound has travelled twice
                                                                        # the distance we need to measure (sound out,
                                                                        # bounced off object, sound returned)

    distancef = (time2 - time1) / 0.00000295 / 2 / 10                    # Convert the timer values into centimetres
    return (distancef)                                                   # Exit with the distance in centimetres
    gpio.cleanup()

##while True:
##    dis_f = get_distancef()
##    print "distance:", dis_f
