#Retrieve latitude and longitude of a given location

import json
import urllib.request , urllib.parse

city= input("eneter city name: ")
url='http://api.weatherstack.com/current?'

#acess api key
with open('weatherAPI.txt','r') as f:
    api_key=f.read()
    
params = {}
params['access_key']=api_key
params['query']=city    
#Create service url
#service_url = url + urllib.parse.urlencode({'access_key': api_key}) +'&'+ urllib.parse.urlencode({'query': city})
service_url = url + urllib.parse.urlencode(params)

#Print genearted service url !Remeber it contains the api key
print(service_url) 


data = urllib.request.urlopen(service_url).read()

#decode data to string
info=data.decode()

js=json.loads(info)

#print(js)
finalInfo = f"""
Location : {js["location"]["name"]}
Country : {js["location"]["country"]}
Region : {js["location"]["region"]}
Observation Time : {js["current"]["observation_time"]}
Temperature :{js["current"]["temperature"]}
Weather Description : {js["current"]["weather_descriptions"]}
Humdidity : {js["current"]["humidity"]}
"""

print(finalInfo)
