import requests
import json

webhook_url = 'https://webhook.site/8d71c288-75dd-4b2f-b500-48ef07284f34'

data = { 'name': 'Benjamin',
         'age': 37,
         'message': 'webhook caught!!!',
         'status' : 'triggering'
         }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
