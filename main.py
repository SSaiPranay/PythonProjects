#11-10-2026

from fastapi import FastAPI
from app.api.documents import router as documents_router

app = FastAPI(title="GenAI document Service")


app.include_router(documents_router)



@app.get("/")
async def root()-> dict[str,str]:
    return {"message":"Hello World!!!"}

@app.get("/health")
async def health()-> dict[str,str]:
    return {"status":"healthy"}

@app.get("/tasks")
async def tasks()-> dict[str,str]:
    return {"tasks":["task A","task B","task C"]}

#11-10-2026