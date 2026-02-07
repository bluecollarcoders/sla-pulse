from fastapi import FastAPI
# Import the FastAPI class so we can create a web application object.

app = FastAPI(title="SLA Pulse", version="0.1.0")
# Create the main FastAPI application instance.
# - app is the object the server (like Uvicorn) will run.
# - title and version are just metadata for docs/OpenAPI, etc.

@app.get("/health")
# This is a decorator.
# It tells FastAPI:
#   "The function right below handles GET requests to the /health path."

def health() -> dict[str, str]:
        # Define a normal Python function named 'health'.
    # -> dict[str, str] is a type hint:
    #   "this function returns a dict whose keys are strings and values are strings."

    return {"status": "ok"}
    # Actual return value: a small dict with one key "status" and value "ok".
    # FastAPI will automatically convert this dict to JSON: {"status": "ok"} for the HTTP response.
