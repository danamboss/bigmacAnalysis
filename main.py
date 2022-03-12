from flask import Flask, render_template
from bigmacs import get_data 

app = Flask('app')

@app.route('/')
def hello_world():
  data = get_data()
  sweden, isreal, egypt, china = [], [], [], []

  for item in data:
    swe = data[0]['country_name']

    sweden.append(swe)

    print(sweden)
  
  return render_template("index.html")

app.run(host='0.0.0.0', port=8080, debug=True)
