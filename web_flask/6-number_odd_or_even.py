#!/usr/bin/python3
"""starts flask"""

from flask import Flask
from flask import render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ptext(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def poopla(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
"""displays page only if number is an int"""
def num_temp(n):
    return render_template('5-number.html')


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
"""displays page if numbre is an int"""
def num_parity(n):
    if n % 2 == 0:
        string = "even"
    else:
        string = "odd"
    return render_template('6-number_odd_or_even.html', n = n, string = string)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
