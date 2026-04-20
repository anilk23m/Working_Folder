#Everythin around you is object -
#object has 2 thing -
#atrribute(properties/data) and methods(action/behavior)

#car - brand/color/speed/model/fuel - start(), accelerate(), stop(), brake()

#class -
#object - real thing (actual car on the road)
#class - blueprint (design plan for the car)

#factory has a blueprint (class)
#factory use blueprint to manufacture
#actual car come out (object/instance)

#one blueprint - many cars
#one class - many objects

class Car:
    def start(self):
        print("Car is running")
    def stop(self):
        print("Car is stopped")
    def accelerate(self):
        print("Car is accelerating")
    def brake(self):
        print("Car is braking")
car1 = Car() #we created the first object
car1.start()
car1.accelerate()
car1.brake()
car1.stop()