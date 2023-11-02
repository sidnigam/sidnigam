import time
from flask import Flask

app = Flask(__name__)

def bold(function):
    def wrapper(*args, **kwards):
        return f"<b> test-wrapper {function()} </b>"
    return wrapper

@app.route("/")
@bold
def hello_world():
    return "<p>Hello, World! test</p>"

@app.route("/bye")
def adios():
    return "<h1>bye <b> bye </b> </h1>"

@app.route("/<name>/<int:num>")
@bold
def greet(name, num):
    return f"<h1 style='text-align: center'>Hello {name} </h1>" \
            f"<h2>How are you? <div> Magic number is {num}</h2> <p> bye </p>" \
            f"<div style='text-align: center'> <img width=300 src = 'https://media2.giphy.com/media/wKQRIoFXsQIGA/giphy.gif?cid=ecf05e47pysxm2f444buhhtqnd6s9gmuedevu8wlfslqjv31&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"

if __name__ == "__main__":
    app.run(debug=True)
