# File: app.py

# This is a simple Flask web application that responds with "Hello, Docker!" when you visit the homepage.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)