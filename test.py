import datetime
import random
import string

from flask import Flask, request, Response
from webargs.flaskparser import use_kwargs
from webargs import fields, validate

from html_formatters import format_list
from utils import generate_password, get_current_time, generate_students

app = Flask(__name__)

from flask import jsonify
@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello():
    return "<p>Hello???</p>"

@app.route("/now")
def now():
    return str(get_current_time())

@app.route("/random")
@use_kwargs({
    "length": fields.Int(
            required=False,
            missing=100,
            validate=[validate.Range(min=1, max=999)]
        ),
    "digits": fields.String(
        required=True,
        # missing=100,
        validate=[validate.Range(min=1, max=999)]
    )},
    location="query"
)
def get_random(length):
    return generate_password(length)

@app.route("/students")
def get_students():
    students = generate_students(10)
    result = format_list(students)
    return result

app.run(debug=True, port=5001)
