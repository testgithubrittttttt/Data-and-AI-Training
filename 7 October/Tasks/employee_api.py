from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


# Pydantic model
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float


# In-memory employee list with 3 sample employees
employees: List[dict] = [
    {"id": 1, "name": "Alice Johnson", "department": "HR", "salary": 50000.0},
    {"id": 2, "name": "Bob Smith", "department": "Engineering", "salary": 75000.0},
    {"id": 3, "name": "Charlie Brown", "department": "Sales", "salary": 62000.0}
]


# ------------------- GET all employees -------------------
@app.get("/employees")
def get_all_employees():
    return employees


# ------------------- GET single employee -------------------
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


# ------------------- POST: Add new employee -------------------
@app.post("/employees", status_code=201)
def add_employee(employee: Employee):
    # Check for duplicate ID
    for emp in employees:
        if emp["id"] == employee.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")

    employees.append(employee.dict())
    return {"message": "Employee added successfully", "employee": employee}


# ------------------- PUT: Update employee -------------------
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated_employee: Employee):
    for i, emp in enumerate(employees):
        if emp["id"] == emp_id:
            employees[i] = updated_employee.dict()
            return {"message": "Employee updated", "employee": updated_employee}

    raise HTTPException(status_code=404, detail="Employee not found")


# ------------------- DELETE: Remove employee -------------------
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    for i, emp in enumerate(employees):
        if emp["id"] == emp_id:
            deleted_emp = employees.pop(i)
            return {"message": "Employee deleted", "employee": deleted_emp}

    raise HTTPException(status_code=404, detail="Employee not found")


# ------------------- BONUS: Count of employees -------------------
@app.get("/employees/count")
def count_employees():
    return {"count": len(employees)}
