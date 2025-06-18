from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
# router
from api.v1 import routerV1

app = FastAPI (title="RealEstate API", version="0.1.0")

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


app.include_router (routerV1, prefix='/api/v1')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)