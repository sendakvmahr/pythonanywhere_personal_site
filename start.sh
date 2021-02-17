#!/bin/sh
export FLASK_DEBUG=True
export FLASK_APP=flask_app.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
