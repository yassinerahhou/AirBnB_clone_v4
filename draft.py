#!/usr/bin/python3

"""C is fun"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """first route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_world_hbnb():
    """s route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_hbnb(text):
    """route with varable"""
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def txt_py(text):
    text = text.replace("_", " ")
    if text is None:
        text = 'is cool'
        """ Prints a Message when /python is called """
        return (f"Python {text}")
    else:
        """ Prints a Message when /python is called """
        return (f"Python {text}")


@app.route('/number/<int:n>', strict_slashes=False)
def numbern(n):
    """ Prints a number when /pythonnumber is called """

    return (f"{n} is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def disphtml(n):
    """ Prints html page whene number templateis called """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>',  strict_slashes=False)
def evenorodd(n):
    if n % 2 == 0:
        isx = 'even'
    else:
        isx = 'odd'
    """ Prints html page whene number templateis called """
    return render_template("6-number_odd_or_even.html", n=n, isx=isx)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
