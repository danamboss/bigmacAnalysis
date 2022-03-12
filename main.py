from flask import Flask, render_template
from bigmacs import get_data 
import pygal
from pygal.style import DarkSolarizedStyle


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
    swed = round(data[0]['dollar_ppp'], 2)
    isrd = round(data[1]['dollar_ppp'], 2)
    egyd = round(data[2]['dollar_ppp'], 2)
    chnd = round(data[3]['dollar_ppp'], 2)
    sweb = data[0]['burger']
    isrb = data[1]['burger']
    egyb = data[2]['burger']
    chnb = data[3]['burger']

    pppno = [swed, isrd, egyd, chnd]
    bar_chart = pygal.Bar(fill=True, interpolate='cubic', style=DarkSolarizedStyle)
    bar_chart.y_labels = map(str, range(0, 20))
    bar_chart.x_labels = ['Sweden', 'Isreal', 'Egypt', 'China']
    bar_chart.add('Price Comparison', pppno)
    bar_chart.render_to_file('static/bar_chart.svg')

    # sweden.append(swe)

    # print(sweden)
  
  return render_template("index.html", swe=swe, isr=isr, egy=egy, chn=chn, swed=swed, isrd=isrd, egyd=egyd, chnd=chnd, sweb=sweb, isrb=isrb, egyb=egyb, chnb=chnb)

app.run(host='0.0.0.0', port=8080, debug=True)
