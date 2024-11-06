class vehicle:
    def __init__(self, colour):
        self.warna = colour
        self.wheelDiameter = 19
    def __str__(self):
        return("this vehicle's colour is " + self.warna)
    def move(self):
        print("vroom vroom")
class car(vehicle):
    def __init__(self, colour):
        self.numbaofWheels = 4
        self.__secret = "secret" 
        vehicle.__init__(self, colour)
    def ngedrift(self):
        print("drift drift")
    def showsecret(self):
        print(self.__secret)
coupe = vehicle("yellow")
chevvy = car("colour")
chevvy.move()
