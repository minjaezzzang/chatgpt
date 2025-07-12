import sys
def run_file(path: str):
    import subprocess
    import sys

    try:
        subprocess.run([sys.executable, path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {path}: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == "__main__":
    setup_path = 'setup_ollama_models.py'
    try:
        run_file(setup_path)
    except FileNotFoundError:
        print(f"File {setup_path} not found.", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"{setup_path} executed successfully.")
        sys.exit(0)
    
