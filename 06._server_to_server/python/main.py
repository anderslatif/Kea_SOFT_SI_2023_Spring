from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/date")
def get_date():
    return datetime.now()

