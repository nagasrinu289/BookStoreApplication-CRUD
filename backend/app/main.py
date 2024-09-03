from fastapi import FastAPI
from .database import engine, Base
from .routers import books
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

@app.get('/')
def show():
    return "hello"

app.include_router(books.router)
