from pydantic import BaseModel


class Student(BaseModel):
    name: str

    age: int

    email: str

    isActive: bool = True


data = {"name": "Dhruv", "age": 22, "email": "dhruv@gmail.com"}

student = Student(**data)

print(student)

print(student.name)

'''invalid_data= {"name":"dhruv", "age":"twenty", "email":"dhruv@gmail.com"}

student= Student(**invalid_data)'''
