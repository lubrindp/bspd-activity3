from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to flask home JR!"

@app.route('/page1')
def page1():
    return "Welcome to flask page1 JR!"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)