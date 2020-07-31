from flask import Flask
from dotenv import load_dotenv
from pathlib import Path

app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

@app.route('/')
def hello_world():
    return "Hola, Mundo"

if __name__ == "__main__":
    app.run()    