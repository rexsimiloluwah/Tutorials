"""
    main.py : Main app file
"""

import uvicorn
from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.middleware.cors import CORSMiddleware 
import schemas
from routes.shorten import router as ShortenRouter
from routes.redirect import router as RedirectRouter
from mongoengine import connect, disconnect, errors
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from decouple import config

MONGO_URI = config('MONGO_URI')

print(MONGO_URI)

app = FastAPI()

# Templates
templates = Jinja2Templates(directory = "templates")


@app.get("/", response_class = HTMLResponse)
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request" : request})

app.include_router(ShortenRouter, tags = ["Shorten long URL"], prefix = "/api/v1/shorten")

app.include_router(RedirectRouter, tags = ["Redirect to Short URL"])

@app.on_event("startup")
async def create_db_client():
    try:
        connect(host = MONGO_URI)
        print("Successfully connected to Mongo Atlas database.")
    except Exception as e:
        print(e)
        print("An error occurred while connecting to Mongo Atlas database.")

@app.on_event("shutdown")
async def shutdown_db_client():
    pass

if __name__ == "__main__":
    uvicorn.run(app, host  = "0.0.0.0", port = 5000)