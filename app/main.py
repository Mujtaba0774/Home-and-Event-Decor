from fastapi import FastAPI
from . import models
from database import engine
from routes import router as api_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()

# Include the API routes
app.include_router(api_router)

# Define a root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the Home and Event Decoration"}
