import urllib.parse
from flask import *
import requests
import random

app = Flask('name')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
@app.route('/', methods=['GET'])
def home_page():
  email=request.args.get("email")
  pas=request.args.get("pass")
  url = 'https://api.fanduel.com/sessions'
  headers = {
  'authority': 'api.fanduel.com',
  'scheme': 'https',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
  'authorization': 'Basic ZWFmNzdmMTI3ZWEwMDNkNGUyNzVhM2VkMDdkNmY1Mjc6',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'https://www.fanduel.com',
  'referer': 'https://www.fanduel.com/',
  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
  'x-brand': 'FANDUEL'
  }
  data = {
  'email': email,
  'password': pas,
  'product': 'DFS'
  }
  proxy = {
  "http": "us.proxiware.com:2000",
  "https": "us.proxiware.com:2000"
  }
  response = requests.post(url, headers=headers, json=data, proxies=proxy)
  print(response.status_code)
  re=response.json()
  
  return re
    
app.run(host="0.0.0.0")
