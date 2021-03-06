import os
import nasdaqdatalink
import pandas as pd
import json
import urllib.request


my_secret = os.environ['ndqkey']
nasdaqdatalink.ApiConfig.api_key = my_secret
def get_data():
  countries = ["SWE","ISR","EGY","CHN"]
    
  data_list = []
    
  for country in countries:
      data = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{country}', start_date='2021-01-31', end_date='2022-01-31')

            
      url = f'https://restcountries.com/v3.1/alpha/{country}'
      request = urllib.request.urlopen(url)
      result = json.loads(request.read())
      number = float(round(data.iloc[0,3],2))
      ##print(number, type(number))
      
      burger = "🍔" * (int(number)) 
      country = {
        "country":country,
        "local_price": data.iloc[0,0],
        "dollar_ex": data.iloc[0,1],
        "dollar_price": data.iloc[0,2],
        "dollar_ppp": data.iloc[0,3],
        "dollar_valuation":data.iloc[0,4],
        "dollar_adj_valuation":data.iloc[0,5],
        "flag":result[0]["flags"]["png"],
        "country_name":result[0]["name"]["common"],
        "currencies":result[0]["currencies"],
        "burger":burger
      }
      data_list.append(country)


      ##data_list.append(burger)
    
  return data_list
