"""
https://api.nasa.gov address
NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth Asteroid
information. With NeoWs a user can: search for Asteroids based on their closest approach date to Earth,
lookup a specific Asteroid with its NASA JPL small body id, as well as browse the overall data-set.
"""

import requests
import datetime
import csv

url_feed = "https://api.nasa.gov/neo/rest/v1/feed?"

url_neo = "https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=DEMO_KEY"
api_key = "6DObplzvCgGiHB9rpCZehEWQdUs4cS89PX6te8Ad"
finish_date = "2016-07-30"

start_date = "2016-07-01"
while start_date <= finish_date:
    start_date = input("Please Enter Start Date: ")
    end_date = input("Please Enter End Date: ")
    finish_date = '2016-07-30'

    response = requests.get(url_feed, params={
        "start_date":start_date,
        "end_date":end_date,
        "api_key":api_key
    })

    nasa = response.json()
    print(response.url)

    liste = []
    for i in (nasa["near_earth_objects"]).keys():
        liste.append(i)


    print("****************************************************")

    liste = list(nasa["near_earth_objects"])
    liste.sort()

    liste1 = []
    for i in liste:
        new_list = nasa['near_earth_objects'][i]

        for i in new_list:
            #print(i["id"], i["is_potentially_hazardous_asteroid"])
            if i["is_potentially_hazardous_asteroid"]==False:
                liste1.append(i["id"])
                liste1.append(i["is_potentially_hazardous_asteroid"])


    #print(i["is_potentially_hazardous_asteroid"])
    with open("asteroid.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "is_potentially_hazardous_asteroid"])
        writer.writerow(liste1)












