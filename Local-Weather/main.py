import requests,bs4
name=input("Enter location\n");
print("Wait...")
try:
    res=requests.get("http://maps.google.com/maps/api/geocode/json",params={'address':name})
    lat=res.json()['results'][0]['geometry']['location']['lat']
    long=res.json()['results'][0]['geometry']['location']['lng']
    link="https://api.darksky.net/forecast/94f3df5dac93c73774df3d273af106fa/"+str(lat)+","+str(long)
    res=requests.get(link)
    print("Temperature: "+str(res.json()['currently']['temperature']))
    print("Humidity: "+str(res.json()['currently']['humidity']))
    print("Wind Speed: "+str(res.json()['currently']['windSpeed']))
    print("Current Forecast: "+str(res.json()['currently']['summary']))
    print("Today's Forecast: "+str(res.json()['hourly']['summary']))
    print("Week's Forecast: "+str(res.json()['hourly']['summary']))
except:
    print("There was some error. Check name or internet connection")
input("\n\nPress enter key to quit")
