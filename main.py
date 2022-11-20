from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.route("/ping")
async def index(req: Request):
    return JSONResponse(content={"message": "pong"})

