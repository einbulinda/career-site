from flask import Flask

# Creates a flask application
app = Flask(__name__)


# Register routes
@app.route('/')
def hello_world():
    return "Hello World Now"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
