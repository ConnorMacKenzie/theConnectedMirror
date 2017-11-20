import forecastio
import json
import StringIO

apikey = "566169fcb4282ff1c9d716df2ccdfd90"
lat = 45.411572
lng = -75.698194
forecast = forecastio.load_forecast(apikey, lat, lng)

curr = forecast.currently()

summ = json.dumps(["It is currently " + curr.summary])

summ = summ +

summ = summ + json.dumps(["It is currently " + curr.summary])
print ("At a temperature of " + str(curr.temperature) + " with a " + str(curr.humidity*100) + " percent humidity")
if curr.precipProbability > 0:
    print ("There is a " + str(curr.precipProbability*100) + " percent chance of " + curr.precipType)
