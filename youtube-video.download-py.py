import yt_dlp

def baixar_video(url, caminho_destino='.'):
    try:
        ydl_opts = {
            'format': 'best',  # Melhor qualidade disponível
            'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',  # Nome do arquivo
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Baixando: {url}")
            ydl.download([url])
            print("Download concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    url = input("Insira a URL do vídeo do YouTube: ")
    caminho_destino = input("Insira o caminho de destino (pressione Enter para salvar no diretório atual): ") or '.'
    baixar_video(url, caminho_destino)
