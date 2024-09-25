
# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Maggie Jiang                                                 #
# 	Created:      03/26/2024, 4:07:23 p.m.                                     #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Define the controller
controller1 = Controller(ControllerType.PRIMARY)
# controller2 = Controller(ControllerType.PARTNER)

# Define Motors
# variable = Motor(port number, gear ratio (green=18-1, red=36-1, blue=6-1), reverse)

leftMotor = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
rightMotor = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(leftMotor, rightMotor)

armMotor1 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
armMotor2 = Motor(Ports.PORTS10, GearSetting.RATIO_18_1, True)
clawMotor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)

#inertialSensor = Inertial(Ports.PORT9)

def drivercontrol():
    leftMotor.spin(FORWARD, controller1.axis3.position()/1.1 + (controller1.axis1.position() / 4), PERCENT)
    rightMotor.spin(FORWARD, controller1.axis3.position()/1.1 - (controller1.axis1.position() / 4), PERCENT)
    armMotor.set_stopping(HOLD)

    if (controller1.buttonL1.pressing()):
        armMotor1.spin(REVERSE, 100, PERCENT)
        armMotor2.spin(REVERSE, 100, PERCENT)
    elif (controller1.buttonL2.pressing()):
        armMotor1.spin(FORWARD, 100, PERCENT)
        armMotor2.spin(FORWARD, 100, PERCENT)
    else:
        armMotor1.stop()
        armMotor2.stop()

    if (controller1.buttonR1.pressing()):
        clawMotor.spin(REVERSE, 100, PERCENT)
    elif(controller1.buttonR2.pressing()):
        clawMotor.spin(FORWARD, 100, PERCENT)
    else:
        clawMotor.stop()

while True:
    drivercontrol()

        
