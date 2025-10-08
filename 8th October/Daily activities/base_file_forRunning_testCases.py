from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float

employees = [
    {"id": 1, "name": "Amit Sharma", "department": "HR", "salary": 50000},
]

@app.get("/employees")
def get_all():
    return employees

@app.post("/employees", status_code=201)
def add_employee(employee: Employee):
    employees.append(employee.dict())
    return employee

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")
