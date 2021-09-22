# TODO: app initialization code?


from flask import (
    Flask, Blueprint, flash, redirect, render_template, request, url_for
)

import os

from filomovie import app

@app.route('/', methods=('GET', 'POST'))
def index():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
