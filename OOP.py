class Programmer:
    def __init__(self , company ,name ,age ,position, salary):
        self.company = company
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

emp1 = Programmer('microsoft','joh' , 21 , 'Full stack developer' , '45LPA')
print(emp1.company)