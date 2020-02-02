from flask import Flask
from config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)

@app.route('/<username>')
def home(username):
    return '<h1>Good Morning %s</h1>' % username

@app.route('/')
def home2():
    return '<h1>Hello world</h1>'

if __name__ == '__main__':
    app.run()