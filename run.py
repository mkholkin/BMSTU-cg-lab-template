import sys
import subprocess

from src.main import main as app

if __name__ == "__main__":
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    app()
