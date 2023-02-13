from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def _():
    return { "message": "First FastAPI route" }

@app.get("/newroute")
def _():
    print(type({ "message": "This is my second route" }))
    return { "message": "This is my second route" }

