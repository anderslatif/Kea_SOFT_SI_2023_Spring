from fastapi import FastAPI, Request
import azure.functions as func


app = FastAPI()

@app.get("/api/hello/{name}")
async def get_name(name: str):
  return { "name": name }

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req, context)
