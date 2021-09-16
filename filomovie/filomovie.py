# from flask import (
#     Flask, Blueprint, flash, redirect, render_template, request, url_for
# )


from filomovie import app

# bp = Blueprint('filomovie', __name__)

# @bp.route('/', methods=('GET', 'POST'))
@app.route('/', methods=('GET', 'POST'))
def index():
    return "<p>Hello, World!</p>"


