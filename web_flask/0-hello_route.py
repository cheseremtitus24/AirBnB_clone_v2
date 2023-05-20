#!/usr/bin/python3
"""
This module Utilizes basic routes and simple
html display
"""
from flask import Flask
import os
os.environ["FLASK_APP"] = "0-hello_route.py"

# Function that creates the app


app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_world():
    """ Function returns a very basic html string without any tags"""
    return 'Hello HBNB!'


# Create the App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
