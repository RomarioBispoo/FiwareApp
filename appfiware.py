''' https://www.geeksforgeeks.org/get-post-requests-using-python/
	https://codare.aurelio.net/2006/09/20/python-http-get-e-post-com-urllib/
    http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
    https://www.tutorialspoint.com/How-to-convert-JSON-data-into-a-Python-tuple
'''
import requests
import json

def SimpleGetHttp(): # Does a Simple Http Get (without parameters) 
    url = "http://172.18.1.1:1026/v2/entities"
    r = requests.get(url)
    print(r.raise_for_status())
    print(r.status_code)
    print(r.text)
    
def GetHttp(): #does a Get using parameters
    url = "http://172.18.1.3:1028/v2/entities"
    payload = {'Options': 'keyValues','type':'Store'} #returns the data of all Store entities within the context data
    r = requests.get(url, params=payload)
    #print(r.raise_for_status())
    #print(r.status_code)
    print(r.text)
    #print(r.url)
    
def PostHttp():
    url = "http://172.18.1.1:1028/v2/entities"
    headers = {'Content-Type': 'application/json'}
    
    #2 payload from json file, converting the entities for tuples (not running yet)  
    payload1 =  [
        ("id", "urn:ngsi-ld:Store:001"),
        ("type", "Store"),
        ("address",
            [
                ("type", "PostalAddress"),
                ("value",
                    [
                        ("streetAddress", "Bornholmer Straße 65"),
                        ("addressRegion", "Berlin"),
                        ("addressLocality", "Kreuzberg"),
                        ("postalCode", "10969"),
                    ]
                )
            ],
        ),
        ("location",
            [
                ("type", "geo:json"),
                ("value",
                    [
                     ( "type", "Point"),  
                     ("coordinates", [13.3903, 52.5075])
                    ]
                )
            ]
        ),
        ("name",
            [
                ("type", "Text"),
                ("value", "Checkpoint Markt")
            ]
        )
    ]

    # i can do the post request using this method, passing the json entities (working)
    data1 = {"id": "Room6",
  "type": "Room",
  "temperature": {
    "value": 23,
    "type": "Float"
  },
  "pressure": {
    "value": 720,
    "type": "Integer"
  }}
        
    # equals to payload1    
    payload2 = [
                ("type", "Store"),
                ("id", "urn:ngsi-ld:Store:002"),
                ("address",
                	[	
                		("type","PostalAddress"),
                		("value",
                			[
                				("streetAddress", "Friedrichstraße 44"),
                				("addressRegion", "Berlin"),
                				("addressLocality", "Kreuzberg"),
                				("postalCode", "10696")
                			]
                		)  
                		
                	]
               	),
               	("location", 
               		[
               			("type", "geo:json"),
               			("value",
               				[
               					("type", "Point"),
               					("coordinates", [13.3903, 52.5075])
               				]
               			)
               		]
               	),
               	( "name", "Bösebrücke Einkauf")
              ]
    #equals to data1
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
    r1 = requests.patch(url, headers=headers, json=data1)
    #r2 = requests.post(url, headers=headers, json=data2)
    # or this method (using tuples)
    #r3 = requests.post(url, headers=headers, data=payload1)
    #r4 = requests.post(url, headers=headers, json=payload2)
    
    #print(r3.text)
    #print(r4.text)
    print(r1.raise_for_status())
    print(r1.status_code)  
    #print(r2.raise_for_status())
    #print(r2.status_code)    
    #r1 = requests.post(url, data=json.dumps(payload1), headers=headers)
    #r2 = requests.post(url, data=json.dumps(payload2), headers=headers)
    #print(r.text)
    #print(payload2[2][1][0][1][0])
def PacthHttp():
    url = "http://172.18.1.1:1026/v2/entities/Room1/attrs" #patch 
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
    print(r.raise_for_status())
    print(r.status_code)   
#PacthHttp()
#PostHttp()
SimpleGetHttp()
#url = "http://localhost:1026/version"

