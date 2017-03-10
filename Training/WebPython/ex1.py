#!C:\python36\python.exe

'''
Created on 9 Mar 2017

@author: Graham
'''

import requests

url = requests.get("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=46201")

print (url)

ress = url.json()

print(ress)

for result in ress['results']:
    print (result)


market = "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/mktDetail?id="
for result in ress['results']:
    id = result['id']
    details = requests.get(market + id).json()
    # See https://search.ams.usda.gov/farmersmarkets/v1/svcdesc.html
    #print (details['marketdetails']['GoogleLink'])
    print (details['marketdetails']['Schedule'])
