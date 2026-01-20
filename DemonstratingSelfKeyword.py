class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
    
s1 = Student("Rahul", 20)
s2 = Student("Anu", 22)

s1.display()
print("-----")
s2.display()