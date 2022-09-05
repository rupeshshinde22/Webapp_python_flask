from flask import Flask

app = Flask(__name__)


# defined routes
@app.route('/')
def index():
    return "FLASK PROJECT"


@app.route('/about')
def about():
    return "ABOUT FLASK PROJECT"
