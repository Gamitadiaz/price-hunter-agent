from fastapi import FastAPI
 
app = FastAPI() # Create a FastAPI instance
@app.get("/health") # Define a GET endpoint at /health
def health_check():
    return {"status": "ok"} # Return a JSON response indicating the service is alive