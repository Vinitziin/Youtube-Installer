import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.downloader import baixar_video

router = APIRouter(
    prefix="/download",
    tags=["download"],
)

class DownloadRequest(BaseModel):
    url: str
    formato: str = "mp4"  
    qualidade: str = "best"  

@router.post("/")
async def download_video(request: DownloadRequest):
    """
    Endpoint para baixar um vídeo do YouTube.
    """
    try:
        # Baixa o vídeo
        caminho_arquivo = baixar_video(request.url, request.formato, request.qualidade)
        if not caminho_arquivo:
            raise HTTPException(status_code=500, detail="Falha ao baixar o vídeo.")
        
        # Extrai apenas o nome do arquivo
        nome_arquivo = os.path.basename(caminho_arquivo)
        
        return {"message": "Download concluído!", "file_path": nome_arquivo}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
