from fastapi import FastAPI,Header
app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World"

@app.get("/sum/{a}")
def sumation(a:int,b:int,c:int=Header()):
    return a+b+c
