student = {
    "name" : "alice",
    "age" : 19,
    "height" : 80
}
print(student["name"])#first way of accessing the value
print(student.get("name"))#first way of accessing the value

#updating the dictionary

student["grade"] = "A"#adding new value
student["name"] = "Dhruv"#updating the existing ones

print(student["name"])
print(student["grade"])

student.pop("grade")#removing by key

print(student)#delete key

for key, value in student.items():#unpacking of the dictionary
    print(key,value)

del student["name"]
print(student)
