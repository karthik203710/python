class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

obj = Student("Karthik")
obj.display()