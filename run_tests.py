import sys
import subprocess

if __name__ == "__main__":
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    subprocess.check_call([sys.executable, "-m", "pytest", "tests/"])
