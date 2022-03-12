from flask import Flask, render_template
from bigmacs import get_data 

app = Flask('app')

@app.route('/')
def hello_world():
  data = get_data()
  sweden, isreal, egypt, china = [], [], [], []

  for item in data:
    swe = data[0]['country_name']
    isr = data[1]['country_name']
    egy = data[2]['country_name']
    chi = data[3]['country_name']
    sweden.append(swe)
    isreal.append(isr)
    egypt.append(egy)
    china.append(chi)
    print(sweden)
    print(isreal)
    print(egypt)
    print(china)
  
  return render_template("index.html")

app.run(host='0.0.0.0', port=8080, debug=True)
