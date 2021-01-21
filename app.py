from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os


SECRET_KEY = os.getenv("EMAIL")

app = Flask(__name__)


@app.route('/')
def hello_world():
    return SECRET_KEY


if __name__ == '__main__':
    app.run()
