import os
import shutil

def limpar_arquivos_temp(diretorio="./downloads", dias=1):
    """
    Remove arquivos mais antigos que `dias` no diretório especificado.
    """
    try:
        for arquivo in os.listdir(diretorio):
            caminho = os.path.join(diretorio, arquivo)
            if os.path.isfile(caminho):
                # Verifica a idade do arquivo
                if (os.stat(caminho).st_mtime < (time.time() - dias * 86400)):
                    os.remove(caminho)
    except Exception as e:
        print(f"Erro ao limpar arquivos temporários: {e}")
