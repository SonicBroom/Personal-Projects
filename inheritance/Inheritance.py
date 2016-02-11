class SteeringWheel(object):
    def __init__(self, angle=0):
        self.wheelAngle = angle

    def turnWheel(self, angle):
        self.wheelAngle = angle

    def getWheelAngle(self):
        return self.wheelAngle

class Radio(object):
    def __init__(self, state="off"):
        self.radioState = state

    def turnRadioOn(self):
        self.radioState = "on"

    def turnRadioOff(self):
        self.radioState = "off"

class Car(object):
    def __init__(self, color="black"):
        self.carColor = color
        self.carSteeringWheel = SteeringWheel()
        self.carRadio = Radio()

class BMW(Car):
    def __init__(self, color="silver"):
        Car.__init__(self, color)
        self.myColor = color

myCar = BMW()
myCar.carSteeringWheel.turnWheel(90)

print ("Car Steering wheel angle: ", myCar.carSteeringWheel.getWheelAngle())


