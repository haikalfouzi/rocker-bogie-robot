import RPi.GPIO as gpio
import time
gpio.setwarnings(False)

def get_distancel ():
    gpio.setmode (gpio.BCM)
    trigl = 24 #16 26
    echol = 20 #21
    gpio.setup(trigl,gpio.OUT)
    gpio.setup(echol,gpio.IN)
    if gpio.input (echol):                                               # If the 'Echo' pin is already high
        return (100)                                                    # then exit with 100 (sensor fault)

    distancel = 0                                                        # Set initial distance to zero

    gpio.output (trigl,False)                                            # Ensure the 'Trig' pin is low for at
    time.sleep (0.05)                                                   # least 50mS (recommended re-sample time)
    gpio.output (trigl,True)                                             # Turn on the 'Trig' pin for 10uS (ish!)
    gpio.output (trigl,False)                                            # Turn off the 'Trig' pin
    time1, time2 = time.time(), time.time()                             # Set inital time values to current time

    while not gpio.input (echol):                                        # Wait for the start of the 'Echo' pulse
        time1 = time.time()                                             # Get the time the 'Echo' pin goes high
        if time1 - time2 > 0.02:                                        # If the 'Echo' pin doesn't go high after 20mS
            distancel = 100                                              # then set 'distance' to 100
            break                                                       # and break out of the loop

    if distancel == 100:                                                 # If a sensor error has occurred
        return (distancel)                                               # then exit with 100 (sensor fault)

    while gpio.input (echol):                                            # Otherwise, wait for the 'Echo' pin to go low
        time2 = time.time()                                             # Get the time the 'Echo' pin goes low
        if time2 - time1 > 0.02:                                        # If the 'Echo' pin doesn't go low after 20mS
            distancel = 100                                              # then ignore it and set 'distance' to 100
            break                                                       # and break out of the loop

    if distancel == 100:                                                 # If a sensor error has occurred
        return (distancel)                                               # then exit with 100 (sensor fault)

                                                                        # Sound travels at approximately 2.95uS per mm
                                                                        # and the reflected sound has travelled twice
                                                                        # the distance we need to measure (sound out,
                                                                        # bounced off object, sound returned)

    distancel = (time2 - time1) / 0.00000295 / 2 / 10                    # Convert the timer values into centimetres
    return (distancel)                                                   # Exit with the distance in centimetres
    gpio.cleanup()
    
##while True:
##    dis_l = get_distancel()
##    print "distance:", dis_l