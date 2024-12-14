from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes.download import router as download_router
import os


app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

if not os.path.exists("downloads"):
    os.makedirs("downloads")

app.mount("/files", StaticFiles(directory="downloads"), name="downloads")

app.include_router(download_router)

@app.get("/")
def read_root():
    return {"message": "API de Download do YouTube está funcionando!"}
