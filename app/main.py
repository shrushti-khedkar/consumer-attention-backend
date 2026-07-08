from fastapi import FastAPI

from app.core.database import Base, engine
from app.models import models
from app.api import auth, layout

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Consumer Attention Mapping System")

app.include_router(auth.router)
app.include_router(layout.router)


@app.get("/")
def read_root():
    return {"message": "Consumer Attention Mapping System is running!"}