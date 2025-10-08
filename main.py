from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"Message": "Hello Atul CICD First Chang"}


@app.get("/user/{name}")
def get_name(name):
    return {"message": f"Hello my name is {name}"}
