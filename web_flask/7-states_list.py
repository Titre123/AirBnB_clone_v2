#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state():
    '''render states '''
    return render_template('7-states_list.html',
                           store=storage.all(State).values())


@app.teardown_appcontext
def teardown(self):
    ''' Teardown storage '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
