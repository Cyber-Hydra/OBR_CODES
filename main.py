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
sesq = ColorSensor(Port.S1)
sdir = ColorSensor(Port.S2)
mdir = Motor(Port.A)
mesq = Motor(Port.B)
robot = DriveBase(mesq, mdir, 55.5, 160)

###         ###         ###         ###         ###         ###         ###         ###         ###         ###         
def SeguirLinha(condicao):
    while(condicao==False):
        while(sesq.color()==WHITE and sdir.color()==WHITE):
            robot.drive()
        robot.stop()
        if(sesq.color()==BLACK):
            if(sdir.color()==BLACK):
                robot.straight(10)
            robot.turn(3)
        else:
            robot.turn(-3)
# Write your program here.
ev3.speaker.beep()

SeguirLinha(FALSE)
