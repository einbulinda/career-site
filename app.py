from flask import Flask, render_template, jsonify

# Creates a flask application
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Nairobi Kenya',
        'salary': 400_000
    },
    {
        'id': 2,
        'title': 'Software Developer',
        'location': 'Nairobi Kenya',
        'salary': 240_000
    },
    {
        'id': 3,
        'title': 'UX Designer',
        'location': 'Nairobi Kenya',
        'salary': 140_000
    },
]


# Register routes
@app.route('/')
def hello_world():
    # Pass the JOBs list to the template as an argument
    return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs') #API Route
def jobs_api():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
