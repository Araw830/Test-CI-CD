from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"Message": "Hello Atul CICD First Chang"}
