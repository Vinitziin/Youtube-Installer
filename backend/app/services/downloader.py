import yt_dlp

def baixar_video(url, formato_saida='mp4', qualidade='best'):
    """
    Baixa um vídeo do YouTube com base no link, formato e qualidade desejados.
    """
    try:
        ydl_opts = {
            'format': qualidade,
            'outtmpl': './downloads/%(title)s.%(ext)s',
            'merge_output_format': formato_saida,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            arquivo_saida = ydl.prepare_filename(info)
            return arquivo_saida.replace("\\", "/")
    except Exception as e:
        raise Exception(f"Erro ao baixar vídeo: {e}")
