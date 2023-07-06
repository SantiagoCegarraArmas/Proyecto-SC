import requests

def endpointjson():
  url='https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json'
  response=requests.request('GET',url)
  return response.json()