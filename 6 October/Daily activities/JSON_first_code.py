import json

#python directory
student = {
    "name":"rahul",
    "age":21,
    "course":["ai","ml","dl"],
    "marks":{"ai":85,"ml":90,"dl":100}
}
with open("student.json","w") as f:
    json.dump(student,f,indent=4)
with open("student.json","r") as f:
    data = json.load(f)
print(data["name"])
print(data["marks"]["ai"])
