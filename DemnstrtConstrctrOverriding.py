class Vehicle:
    def __init__(self):
        print("Vehicle constructor called")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Car constructor called")

c = Car()