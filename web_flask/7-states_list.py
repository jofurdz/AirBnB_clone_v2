#!/usr/bin/python3
"""starts flask"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states_list')
def states_list():
    state = storage.all(State)
    return render_template('7-states_list.html', State=state)

@app.teardown_appcontext
def teardown(context):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
