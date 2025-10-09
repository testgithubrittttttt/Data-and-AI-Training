# app.py
#question - 
✅ A FastAPI backend that serves a GET API returning 5 students

✅ A simple HTML page that fetches this API and shows the student list in the UI

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to call the API from any origin (for demo purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample student data
students = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 21},
    {"id": 3, "name": "Charlie", "age": 22},
    {"id": 4, "name": "Diana", "age": 23},
    {"id": 5, "name": "Ethan", "age": 24},
]

@app.get("/students")
def get_students():
    return students
