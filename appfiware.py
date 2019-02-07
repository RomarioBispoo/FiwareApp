''' https://www.geeksforgeeks.org/get-post-requests-using-python/
	https://codare.aurelio.net/2006/09/20/python-http-get-e-post-com-urllib/
    http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
    https://www.tutorialspoint.com/How-to-convert-JSON-data-into-a-Python-tuple
'''
import requests # install using pip
import json

def SimpleGetHttp(): # Does a Simple Http Get (without parameters) 
    url = "http://172.18.1.1:1026/v2/entities"
    r = requests.get(url)
    print(r.raise_for_status()) # status for debugging
    print(r.status_code)
    print(r.text)
    print(r.url)    
    
def GetHttp(): #does a Get using parameters
    url = "http://172.18.1.1:1026/v2/entities"
    payload = {'Options':'Values','attrs':'pressure'} 
    r = requests.get(url, params=payload)
    print(r.text)
    
def PostHttp(): #post request passing a json file (data1) with the entities definition inside
    url = "http://172.18.1.1:1026/v2/entities"
    headers = {'Content-Type': 'application/json'}
    
    #body request (JSON FILE)
    data1 = {"id": "Room7",
  "type": "Room",
  "temperature": {
    "value": 23,
    "type": "Float"
  },
  "pressure": {
    "value": 720,
    "type": "Integer"
  }}
    data2 = {
    "id": "Room2",
  "type": "Room",
  "temperature": {
    "value": 21,
    "type": "Float"
  },
  "pressure": {
    "value": 711,
    "type": "Integer"
  }
    }
    #use this method                       
    r = requests.post(url, headers=headers, json=data1)
    
def PacthHttp():
    url = "http://172.18.1.1:1026/v2/entities/Room7/attrs" #patch 
    headers = {'Content-Type': 'application/json'}
    
    data = { "temperature": {
    "value": 33.5,
    "type": "Float"
            },
  "pressure": {
    "value": 763,
    "type": "Float"
                }
          }
    r = requests.patch(url, headers=headers, json=data)
  
PostHttp()
SimpleGetHttp()
GetHttp()    
PacthHttp()

