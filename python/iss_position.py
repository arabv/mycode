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

location=result["iss_position"]
lon=location["longitude"]
lat=location["latitude"]
print("\nCurrent position of ISS: ")
print("longitude:",lon)
print("latitude:",lat)

screen=turtle.Screen()
imgPath=r"map.jpg"
screen.bgpic(file="map.jpg")
screen.bgcolor('red')
