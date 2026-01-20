# parent class 1
class Father:
    def father_method(self):
        print("This is Father class method")

# parent class 2
class Mother:
    def mother_method(self):
        print("This is Mother class method")

# Child class (Multiple Inheritance)
class Child(Father, Mother):
    def child_method(self):
        print("This is Child class method")

# Create object of Child class
c = Child()

# Access methods from both parent classes
c.father_method()
c.mother_method()
c.child_method()