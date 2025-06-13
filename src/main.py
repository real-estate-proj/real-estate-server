from email import message
from fastapi import APIRouter, Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRouter

app = FastAPI (title="RealEstate API")

origins = ["*"]

app.add_middleware (
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sub_app = FastAPI ()

@sub_app.get('/testing')
def test_sub_app ():
    return ({"message": "hello world 22222222222"})

@app.get ('/')
def testingRoute ():
    return ({"message": "hello world"})

app.mount ('/t', sub_app)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)