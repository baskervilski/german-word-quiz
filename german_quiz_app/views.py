import flask
from german_quiz_app import app
from german_quiz_app import table
from datetime import datetime as dt
from flask import render_template, request, jsonify, abort

import pandas as pd

@app.route("/")
def hello_world():
    message = "Hello, world!"
    return render_template(
        "index.html",
        title=message,
        date_today=dt.now().strftime("%Y-%m-%d"),
        flask_debug=app.debug,
        app_version=app.config["APP_VERSION"],
        enable_cool_new_feature=True,
    )


@app.route("/input")
def input():
    return render_template("input.html", api_endpoint=app.config['API_ENDPOINT'])


@app.route("/upload_new", methods=['POST'])
def upload_new():
    if not request.json:
        abort(400)

    if 0:
        return request.json, 201
    else:
        #en = request.args.get('en')
        #de = request.args.get('de')
        table.put_item(Item=request.json)
        return jsonify(table.scan()['Items'])

