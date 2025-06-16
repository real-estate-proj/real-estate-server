from email import message
from fastapi import APIRouter, Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRouter

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))


app = FastAPI (title="RealEstate API")

origins = ["*"]

app.add_middleware (
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get ('/')
def testingRoute ():
    return ({"message": "hello world"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)