class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


data = {"name": "Dhruv", "age": 22, "email": "gaurav@gmail.com"}
student = Student(**data)
print(student.name)
