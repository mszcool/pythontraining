#
# Working with JSON data
#

import urllib.request
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    eqJSON = json.loads(data)

    # Access contents of the JSON like any other Python object
    if ( "title" in eqJSON["metadata"] ):
        print(eqJSON["metadata"]["title"])
    
    # Output the number of events, plus magnitude and each event name 
    count = eqJSON["metadata"]["count"]
    print("Number of Earthquakes recently: ", count)
    
    # For each event, print the place where it occured
    for ft in eqJSON["features"]:
        print("--> ", ft["properties"]["place"])
    print("----------------------\n")
    
    # Print the events that only have a magnitude greater than 4
    print("Magnituede larger 4, if any")
    for ft in eqJSON["features"]:
        if ft["properties"]["mag"] >= 4.0:
            print("--> ", ft["properties"]["place"], " with magnitude ", ft["properties"]["mag"])
    print("----------------------\n")

    # Print events where at least 1 person reported feeling something
    print("Felt by people?")
    for ft in eqJSON["features"]:
        feltReports = ft["properties"]["felt"]
        if feltReports != None:
            print("One person felt something for %2.1f: " % ft["properties"]["mag"], feltReports) if (feltReports > 0) else ""

def main():
    # Set the URL to get data from
    requestUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson"
    webRequest = urllib.request.urlopen(requestUrl)
    print("Result code: ", webRequest.getcode())
    if(webRequest.getcode() == 200):
        data = webRequest.read()
        printResults(data)

if __name__ == "__main__":
    main()