# class Programmer:
#     def __init__(self , company ,name ,age ,position, salary):
#         self.company = company
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary

# emp1 = Programmer('microsoft','joh' , 21 , 'Full stack developer' , '45LPA')
# print(emp1.company)


class Factory:
    def __init__(self , BT ,Gear , Color):
        self.BT = BT
        self.Gear = Gear
        self.Color = Color

    def Details(self):
        print(self)
    
class Car(Factory):
    def __init__(self, BT, Gear, Color, Wheels):
        super().__init__(BT, Gear, Color)
        self.Wheels = Wheels

class TwoWheeler(Car):
    def __init__(self, BT, Gear, Color, Wheels,):
        super().__init__(BT, Gear, Color, Wheels)