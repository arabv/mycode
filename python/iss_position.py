#!/usr/bin/env python3
                ###shows numbers of people on ISS at the moment###
import json
import turtle
import urllib.request

url="http://api.open-notify.org/astros.json"
response=urllib.request.urlopen(url)
str_response=response.read().decode("utf-8")
result=json.loads(str_response)

print("People in space:",result["number"])

people=result["people"]
for p in people:
    print(p["name"],"in",p["craft"])


                ###shows position of ISS at the moment###
url="http://api.open-notify.org/iss-now.json"
response=urllib.request.urlopen(url)
str_response=response.read().decode("utf-8")
result=json.loads(str_response)

print("\nCurrent position of ISS: ")
print("longitude:",result["iss_position"]["longitude"])
print("latitude:",result["iss_position"]["latitude"])
