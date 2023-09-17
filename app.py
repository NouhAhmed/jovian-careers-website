from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Nairobi, Kenya',
    'salary': 'ksh. 250,000'
  },
    {
    'id': 2,
    'title': 'Data Engineerin',
    'location': 'Johnsburg, SA',
    'salary': 'ksh. 300,000'
  },
  {
    'id': 3,
    'title': 'Front-end Engineer',
    'location': 'remote'
    
  },
  {
    'id': 4,
    'title': 'Back-end Engineer',
    'location': 'San-francisco USA',
    'salary': 'ksh. 350,000'
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)