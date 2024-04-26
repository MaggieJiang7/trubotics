# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:                                                                    #
# 	Created:      03/26/2024, 4:07:23 p.m.                                     #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import

# Brain should be defined by default
brain=Brain()

# Define the controller
controller1 = Controller(ControllerType.PRIMARY)
# controller2 = Controller(ControllerType.PARTNER)

# Define Motors
# variable = Motor(port number, gear ratio (green=18-1, red=36-1, blue=6-1), reverse)

leftMotor = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
rightMotor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(leftMotor, rightMotor)

clawMotor = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
armMotor = Motor(Ports.PORT16, GearSetting.RATIO_18_1, True)

inertialSensor = Inertial(Ports.PORT9)


def preauton():
    armMotor.set_stopping(HOLD)
    inertialSensor.calibrate()

def autonomous():
    #TODO: make some code that worhesdfsdfs lmao
    leftMotor.spin(FORWARD, controller1.axis3.position()/1.1 + (controller1.axis1.position() / 4), PERCENT)
    rightMotor.spin(FORWARD, controller1.axis3.position()/1.1 - (controller1.axis1.position() / 4), PERCENT)

    if (controller1.buttonL1.pressing()):
        clawMotor0.spin(REVERSE, 100, PERCENT)
    elif (controller1.buttonL2.pressing()):
        clawMotor.spin(FORWARD, 100, PERCENT)
    else:
        clawMotor.stop()
