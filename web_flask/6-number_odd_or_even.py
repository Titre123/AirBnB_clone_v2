#!/usr/bin/python3
''' This route the Hello World Message '''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    ''' Function to display message '''
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello_holberton():
    ''' display HBNB '''
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cProgram(text):
    ''' Display a c message '''
    text_arr = text.split('_')
    new_string = ' '.join(text_arr)
    return 'C {}'.format(new_string)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    ''' Display python message '''
    text_arr = text.split('_')
    new_string = ' '.join(text_arr)
    return 'Python {}'.format(new_string)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' Display Number '''
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    ''' template an Html file '''
    return render_template('5-number.html', no=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddEven(n):
    ''' Display number conditionally '''
    return render_template('6-number_odd_or_even.html', no=n)

if __name__ == '__main__':
	app.run(host="0.0.0.0")
