from flask import Flask, render_template
from bigmacs import get_data 

app = Flask('app')

@app.route('/')
def hello_world():
  data = get_data()
  # sweden, isreal, egypt, china = [], [], [], []

  for item in data:
    swe = data[0]['country_name']
    isr = data[1]['country_name']
    egy = data[2]['country_name']
    chn = data[3]['country_name']
    swed = data[0]['dollar_ppp']
    isrd = data[1]['dollar_ppp']
    egyd = data[2]['dollar_ppp']
    chnd = data[3]['dollar_ppp']
    sweb = data[0]['burger']
    isrb = data[1]['burger']
    egyb = data[2]['burger']
    chnb = data[3]['burger']
    

    # sweden.append(swe)

    # print(sweden)
  
  return render_template("index.html", swe=swe, isr=isr, egy=egy, chn=chn, swed=swed, isrd=isrd, egyd=egyd, chnd=chnd, sweb=sweb, isrb=isrb, egyb=egyb, chnb=chnb)

app.run(host='0.0.0.0', port=8080, debug=True)
