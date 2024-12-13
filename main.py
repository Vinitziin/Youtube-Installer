import yt_dlp

def baixar_video_youtube(url, formato_saida='mp4', qualidade='best'):
    """
    Baixa um vídeo do YouTube com base no link, formato e qualidade desejados.

    Parâmetros:
    - url (str): URL do vídeo do YouTube.
    - formato_saida (str): Formato final do arquivo (padrão: 'mp4').
    - qualidade (str): Qualidade do vídeo (ex.: 'best', 'bestvideo', 'bestaudio').

    Retorna:
    - str: Caminho do arquivo baixado.
    """
    try:
        # Configurações para o downloader
        ydl_opts = {
            'format': qualidade,  # Formato/qualidade do vídeo
            'outtmpl': f'./downloads/%(title)s.%(ext)s',  # Nome do arquivo de saída
            'merge_output_format': formato_saida,  # Formato final (ex.: mp4)
        }

        # Baixa o vídeo usando yt_dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Baixando vídeo: {url}")
            info = ydl.extract_info(url, download=True)
            arquivo_saida = ydl.prepare_filename(info)
            print(f"Download concluído: {arquivo_saida}")
            return arquivo_saida

    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    # URL do vídeo
    video_url = "https://youtu.be/4C0oezQxaes?si=NFwT7shYszQigvQw"
    
    # Configurações desejadas
    formato = 'mp4'
    qualidade = 'bestvideo+bestaudio'  # Melhor vídeo e áudio

    # Chama a função
    caminho_arquivo = baixar_video_youtube(video_url, formato, qualidade)
    print(f"Arquivo salvo em: {caminho_arquivo}")
