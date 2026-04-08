# Starter code for Building REST APIs with FastAPI

# To run this code, you need to install FastAPI and Uvicorn:
# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()

# TODO: Add your endpoints here

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

# To run the server: uvicorn starter_code:app --reload