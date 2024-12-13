from fastapi import FastAPI
from app.routes.download import router as download_router

app = FastAPI(
    title="Youtube Downloader API",
    description="API para baixar vídeos do Youtube",
    version="1.0.0" 
)

app.include_router(download_router)

@app.get("/")
def read_root():
    return {"mensage": "Bem vindo a API de download de vídeos do Youtube!"}

    