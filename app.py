from flask import Flask, render_template

# Creates a flask application
app = Flask(__name__)


# Register routes
@app.route('/')
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
