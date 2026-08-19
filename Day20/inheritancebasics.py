#inheritance
class vehicle:
    def start(self):
        print("vehicle is started")
class car(vehicle):
    def stop(self):
        print("car is stoped")
c1=car()#obj for child class
c1.start()
c1.stop()
