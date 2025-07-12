import urllib as url
import os
import subprocess as sp
import sys
download_url = "https://ollama.com/download/OllamaSetup.exe"
def download_ollama():
    file_name = "OllamaSetup.exe"
    if not os.path.exists(file_name):
        print(f"Downloading {file_name} from {download_url}...")
        url.request.urlretrieve(download_url, file_name)
        print(f"{file_name} downloaded successfully.")
        
    elif os.path.exists(file_name):
        pass
    else:
        print(f"Failed to download {file_name}.")
        return False
    try:
        print(f"Running {file_name}...")
        sp.run([file_name], check=True)
        print('ollama를 설치해주세요(창이 뜨면 "예"를 눌러주세요).')
    finally:
        sp.run(['which', 'ollama'], check=True)
        input("메시지가 떴다면 아무 키나 눌러주세요")
        print("ollama 설치가 완료되었습니다.")
if __name__ == "__main__":
    download_ollama()
    try:
        sp.run([sys.executable, 'setup_ollama_models.py'], check=True)
    except sp.CalledProcessError as e:
        print(f"Error running setup_ollama_models.py: {e}", file=sys.stderr)
        sys.exit(1)  # exit code 1로 종료 (오류 발생 시)
    else:
        print("setup_ollama_models.py executed successfully.")
        sys.exit(0)  # exit code 0로 종료 (성공적으로 실행