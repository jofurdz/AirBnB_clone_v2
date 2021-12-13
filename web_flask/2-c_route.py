#!/usr/bin/python3
"""starts flask"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
