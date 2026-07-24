class Vehicle:
    def __init__(self,brand):
        self.brand = brand

class ElectricCar(Vehicle):
    def __init__(self,brand,battery_capacity):
        super().__init__(brand) #super (сохрани brand и добавь что-то свое)
        self.battery_capacity = battery_capacity
