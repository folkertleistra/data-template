# app.py is used for the creation of the flask server and dash_app. This file allows the user to customize the flask
# server settings.

import dash
from flask import Flask

app = Flask(__name__)
dash_app = dash.Dash(__name__, server=app, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
dash_app.config.suppress_callback_exceptions = True