#for running the test cases your file name must start with - test
from fastapi.testclient import TestClient
from base_file_forRunning_testCases import app #remeber file name must be the which you are checking put that name here

client = TestClient(app)  # Arrange

# ---------------- TEST 1 ----------------
def test_get_all_employees():
    response = client.get("/employees")  # ACT
    assert response.status_code == 200  # Assert
    assert isinstance(response.json(), list)  # Assert

# Arrange ACT Assert -- AAA Pattern
# CICD -- Cont Integration -- Cont Deployment -- checkin -- Build -- Test case -- Deployed to QA Server

# -------------- TEST 2 ------------------
def test_add_employee():
    new_emp = {
        "id": 2,
        "name": "Neha Verma",
        "department": "IT",
        "salary": 60000
    }
    response = client.post(url="/employees", json=new_emp)
    assert response.status_code == 201
    assert response.json()["name"] == "Neha Verma"

# -------------- TEST 3 ------------------
def test_get_employee_by_id():
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Amit Sharma"

# -------------- TEST 4 ------------------
def test_get_employee_not_found():
    response = client.get("/employees/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"

# -------------- TEST: PUT (update employee) ------------------
def test_update_employee():
    # Ensure employee exists: create a fresh employee for this test
    emp = {
        "id": 100,
        "name": "Update Target",
        "department": "Temp",
        "salary": 30000
    }
    post_resp = client.post("/employees", json=emp)
    assert post_resp.status_code in (200, 201)  # allow either depending on implementation

    # Now update that employee's department and salary
    updated = {
        "id": 100,  # can keep same id
        "name": "Update Target",
        "department": "Engineering",
        "salary": 45000
    }
    put_resp = client.put("/employees/100", json=updated)
    assert put_resp.status_code == 200
    body = put_resp.json()
    # depending on your put return shape: check either message + employee or direct employee
    if "employee" in body:
        emp_body = body["employee"]
    else:
        emp_body = body
    assert emp_body["department"] == "Engineering"
    assert emp_body["salary"] == 45000

# -------------- TEST: DELETE (remove employee) ------------------
def test_delete_employee():
    # Create a fresh employee to delete
    emp = {
        "id": 200,
        "name": "Delete Target",
        "department": "Temp",
        "salary": 25000
    }
    post_resp = client.post("/employees", json=emp)
    assert post_resp.status_code in (200, 201)

    # Delete the employee
    del_resp = client.delete("/employees/200")
    assert del_resp.status_code == 200
    del_body = del_resp.json()
    # ensure returned deleted employee id matches
    if "employee" in del_body:
        deleted = del_body["employee"]
    else:
        deleted = del_body
    assert deleted["id"] == 200
    assert deleted["name"] == "Delete Target"

    # Verify it's actually gone
    get_resp = client.get("/employees/200")
    assert get_resp.status_code == 404

# -------------- OPTIONAL: test delete non-existent returns 404 ------------------
def test_delete_non_existent_employee():
    resp = client.delete("/employees/99999")
    assert resp.status_code == 404
