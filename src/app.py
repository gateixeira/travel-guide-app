from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import itinerary

app = FastAPI(title="Travel Guide App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(itinerary.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Travel Guide API!"}