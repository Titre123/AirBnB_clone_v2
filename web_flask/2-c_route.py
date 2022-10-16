#!/usr/bin/python3
''' This route the Hello World Message '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    ''' Function to display message '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_holberton():
    ''' display HBNB '''
    return 'HBNB'


@app.route('/c//<text>', strict_slashes=False)
def C_Program(text):
    text_arr = text.split('_')
    new_string = ' '.join(text_arr)
    return 'C {}'.format(new_string)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
