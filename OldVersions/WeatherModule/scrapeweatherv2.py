# @Author: Theo Hronowsky
# Date: 11/1/2017
#Version 2

import pyowm #library to obtain weather information

owm = pyowm.OWM('2a24bb6134d386f285f790b558aaac5e') # variable owm to contain API key

apiwork = owm.is_API_online() # returns true if API key is working and false if not

if apiwork == False:
    print("API key invalid") # test to see if API key is working 

observation = owm.weather_at_place("Ottawa,On") # variable Observation used to set the location 
w = observation.get_weather() # variable w used to gather the weather data for the location 

time = observation.get_reception_time(timeformat= 'iso') #gets the time of the observation in iso format

temperatureinc = w.get_temperature('celsius')# functions to get temperatures, part of the weather data for a specified location
temperatureinf = w.get_temperature('fahrenheit')

clouds = w.get_clouds()# functions to get conditions, part of the weather data for a specified location

rain = w.get_rain()
snow = w.get_snow()
wind = w.get_wind()

humidity = w.get_humidity() # functions to get additional info, part of the weather data for a specified location
pressure = w.get_pressure()
status = w.get_detailed_status()

sunrise = w.get_sunrise_time('iso') # functions to get sun info as well as tommorows forecast, part of the weather data for a specified location
sunset = w.get_sunset_time('iso')
tomorrow = pyowm.timeutils.tomorrow()


l = observation.get_location() #functions set to variables to get location, latitude, longitude and city ID for the current city that the program is retreiving the weather for
location = l.get_name()
lat = l.get_lat()
lon = l.get_lon()
ID = l.get_ID()

w.to_JSON()#dumping the weather object to JSON and XML
w.to_XML

#Print statements to display all the scaped data for the weather of a city
print("Weather for", location, "at longitude:", lon, "and latitude:", lat "with location ID:", ID, "is:")
print(temperatureinc, "Degrees Celsius,", tempuratureinf, "Degrees Fahrenheit")
print("Todays weather status is:", status)
print("Cloud coverage:", clouds)
print("Rain volume:", rain)
print("Snow volume:", snow)
print("humidity percentage:", humidity, "%")
print(wind)
print(pressure)
print("The sun will rise at:", sunrise)
print("The sun will set at:", sunset)
print("Tommorrows temperature will be:", tommorow)





