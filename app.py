from flask import Flask,render_template

app = Flask(__name__)


#1. defined routes(1st we used it)
# @app.route('/')
# def index():
#     return "FLASK PROJECT"

# 2.but now we are using render_template in routes
# now we have create templates directory as same name because flask look for templates dir so that it can fetch
#  render_template is used to generate output from a template file based
#  on the Jinja2 engine that is found in the application's templates folder.
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return "ABOUT FLASK PROJECT"


#1.Second way to run app.py file is
if __name__ == '__main__':
    app.run(debug=True)
    #write in terminal as :::python app.py