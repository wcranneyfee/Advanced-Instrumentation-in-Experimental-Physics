#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
front_motor = Motor(Port.A)
# back_motor = Moro(Port.B)
touch = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S2)

# Initial speaking 
ev3.speaker.set_volume(100)
ev3.speaker.set_speech_options(language='en', voice='whisperf', pitch=100)

t = True
while t == True:
    front_motor.run(300)

    if touch.pressed() == True:
        front_motor.stop()
 
        yourcolor = color_sensor.color()
        yourcolor = str(yourcolor)

        if yourcolor == 'None':
            pass

        else:
            yourcolor = yourcolor.split('.')[1]


        ev3.speaker.say('I sense' + yourcolor)


        