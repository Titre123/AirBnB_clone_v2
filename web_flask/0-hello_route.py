#!/usr/bin/python3
''' This route the Hello World Message '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    ''' Function to display message '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
