''' https://www.geeksforgeeks.org/get-post-requests-using-python/
	https://codare.aurelio.net/2006/09/20/python-http-get-e-post-com-urllib/
    http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
    https://www.tutorialspoint.com/How-to-convert-JSON-data-into-a-Python-tuple
'''
import requests
import json

def SimpleGetHttp(): # Does a Simple Http Get (without parameters) 
    url = "http://localhost:1026/version/"
    r = requests.get(url)
    print(r.raise_for_status())
    print(r.status_code)
    print(r.text)
    
def GetHttp(): #does a Get using parameters
    url = "http://localhost:1026/v2/entities"
    payload = {'Options': 'keyValues','type':'Store'} #returns the data of all Store entities within the context data
    r = requests.get(url, params=payload)
    #print(r.raise_for_status())
    #print(r.status_code)
    print(r.text)
    #print(r.url)
    
def PostHttp():
    url = "http://localhost:1026/v2/entities"
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
    data1 = {"id": "urn:ngsi-ld:Store:001",
    "type": "Store",
    "address": {
        "type": "PostalAddress",
        "value": {
            "streetAddress": "Bornholmer Straße 65",
            "addressRegion": "Berlin",
            "addressLocality": "Prenzlauer Berg",
            "postalCode": "10439"
        }
    },
    "location": {
        "type": "geo:json",
        "value": {
             "type": "Point",
             "coordinates": [13.3986, 52.5547]
        }
    },
    "name": {
        "type": "Text",
        "value": "Bösebrücke Einkauf"
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
    "type": "Store",
    "id": "urn:ngsi-ld:Store:002",
    "address": {
        "type": "PostalAddress",
        "value": {
            "streetAddress": "Friedrichstraße 44",
            "addressRegion": "Berlin",
            "addressLocality": "Kreuzberg",
            "postalCode": "10969"
        }
    },
    "location": {
        "type": "geo:json",
        "value": {
             "type": "Point",
             "coordinates": [13.3903, 52.5075]
        }
    },
    "name": {
        "type": "Text",
        "value": "Checkpoint Markt"
    }
    }

    #use this method                       
    r1 = requests.post(url, headers=headers, json=data1)
    r2 = requests.post(url, headers=headers, json=data2)
    # or this method (using tuples)
    #r3 = requests.post(url, headers=headers, data=payload1)
    #r4 = requests.post(url, headers=headers, json=payload2)
    
    #print(r3.text)
    #print(r4.text)
    #print(r3.raise_for_status())
    #print(r3.status_code)    
    #r1 = requests.post(url, data=json.dumps(payload1), headers=headers)
    #r2 = requests.post(url, data=json.dumps(payload2), headers=headers)
    #print(r.text)
    #print(payload2[2][1][0][1][0])

PostHttp()
GetHttp()    
#url = "http://localhost:1026/version"

