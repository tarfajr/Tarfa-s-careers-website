from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Security Engineer',
    'location': 'Abuja, Nigeria',
    'salary': 'N800,000'
}, {
    'id': 2,
    'title': 'Software Engineer',
    'location': 'Abuja, Nigeria',
    'salary': 'N750,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'N400,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Jos, Nigeria',
    'salary': 'N350,000'
}]


@app.route('/')
def hello():
    return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
