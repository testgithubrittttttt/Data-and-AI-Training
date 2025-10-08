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

# ------------------- PUT: Update an employee -------------------
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated: Employee):
    """
    Replace the employee with id == emp_id with the provided 'updated' data.
    Uses the path emp_id to find the record; ignores updated.id for lookup
    but will replace the stored record with updated.dict() (including its id).
    """
    for i, emp in enumerate(employees):
        if emp["id"] == emp_id:
            employees[i] = updated.dict()
            return {"message": "Employee updated", "employee": updated}
    raise HTTPException(status_code=404, detail="Employee not found")


# ------------------- DELETE: Remove an employee -------------------
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    """
    Delete the employee with id == emp_id and return the deleted record.
    """
    for i, emp in enumerate(employees):
        if emp["id"] == emp_id:
            deleted = employees.pop(i)
            return {"message": "Employee deleted", "employee": deleted}
    raise HTTPException(status_code=404, detail="Employee not found")
