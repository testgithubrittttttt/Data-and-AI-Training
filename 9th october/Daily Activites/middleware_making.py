from fastapi import FastAPI, Request                      # Import FastAPI class and Request object from fastapi
from fastapi.responses import JSONResponse               # Import JSONResponse to send custom JSON error responses
import logging                                            # Import logging module for logging info and errors
import time                                               # Import time module to measure request duration
import traceback                                          # Import traceback to print exception stack traces for debugging

app = FastAPI()                                           # Create a new FastAPI app instance

# Configure logging to show INFO level and above messages in the console
logging.basicConfig(level=logging.INFO)

# Dictionary to keep track of the number of visits per route/path
visit_counter = {}

# Define custom middleware that will run for every HTTP request
@app.middleware("http")
async def count_visits_middleware(request: Request, call_next):
    start_time = time.time()                              # Record the start time of the request
    path = request.url.path                               # Extract the URL path from the request

    # Increment visit count for the current path, defaulting to 0 if path not present
    visit_counter[path] = visit_counter.get(path, 0) + 1

    try:
        response = await call_next(request)              # Pass the request to the next middleware or endpoint handler
    except Exception as e:
        logging.error(f"Error occurred: {e}")            # Log the error message
        traceback.print_exc()                             # Print the full traceback for debugging
        # Return a JSON response with status 500 Internal Server Error if exception occurs
        return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

    process_time = time.time() - start_time               # Calculate the time taken to process the request
    # Log the path, number of visits to that path, and time taken to process the request
    logging.info(f"Path: {path} | Visits: {visit_counter[path]} | Time taken: {process_time:.4f}s")

    return response                                       # Return the original response back to the client

# Sample endpoint for root URL that returns welcome message and visit count for "/"
@app.get("/")
async def root():
    return {"message": "Welcome!", "visits": visit_counter.get("/", 0)}

# Sample endpoint for "/about" URL that returns about page message and visit count for "/about"
@app.get("/about")
async def about():
    return {"message": "This is the about page.", "visits": visit_counter.get("/about", 0)}

# Sample endpoint "/stats" to return the dictionary of all visit counts for every path
@app.get("/stats")
async def stats():
    return visit_counter
