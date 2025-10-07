# from fastapi import FastAPI
#
# # Create FastAPI instance
# app = FastAPI()
#
# # Root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the FastAPI demo!"}
#
# # Path parameter example
# @app.get("/students/{student_id}")
# def get_student(student_id: int):
#     return {"student_id": student_id, "name": "Rahul", "course": "AI"}

from fastapi import FastAPI

app = FastAPI()

# ------------- GET -------------
@app.get("/students")
def get_students():
    return {"This is a GET request"}

# ------------- POST -------------
@app.post("/students")
def create_student():
    return {"This is a POST request"}

# ------------- PUT -------------
@app.put("/students")
def update_student():
    return {"This is a PUT request"}

# ------------- DELETE -------------
@app.delete("/students")
def delete_student():
    return {"This is a DELETE request"}
