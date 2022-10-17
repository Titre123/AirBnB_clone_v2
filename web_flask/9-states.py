#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


def myFunc(e):
   ''' sorting function '''
   return e['name']


@app.route('/states', strict_slashes=False)
def states():
    '''render states '''
    return render_template('9-states.html',
                           store=storage.all(State).values())


@app.route('/states/<int:id>', strict_slashes=False)
def idState(id):
    ''' render state and city by state id '''
    return render_template('9-states.html',
                           state=storage.all(State)['State.{}'.format(id)],
                           cities=storage.all(State)['State.{}'.format(id).
                           cities, id=id)


@app.teardown_appcontext
def teardown(self):
    ''' Teardown storage '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
