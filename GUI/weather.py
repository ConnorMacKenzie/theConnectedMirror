import forecastio, json, StringIO, socket, sys, time


#when initialized, this class gets information on curent weather
class GetCurrentData:

    #API key given by Forecast.io to access data
    apikey = "566169fcb4282ff1c9d716df2ccdfd90"
    #Latitude and longitude of the SYSC3010 lab
    lat = 45.411572
    lng = -75.698194
    #forcast data object
    forecast = forecastio.load_forecast(apikey, lat, lng, units = "ca")
    #requests forecast of current time
    curr = forecast.currently()

    #Constructor which takes only self as an argument
    def __init__(self):

        #sets variables to the values recieved from Forecast.io
        self.summary = self.curr.summary
        self.icon = self.curr.icon
        self.temp = self.curr.temperature
        self.visibility = self.curr.visibility
        self.windSpeed = self.curr.windSpeed
        self.cloudPercent = self.curr.cloudCover*100
        self.humidity = self.curr.humidity
        self.precipPercent = self.curr.precipProbability*100
        #precipType returns an error if called when percentage of precipitation is 0
        if self.precipPercent > 0:
            self.precipType = self.curr.precipType
        self.pressure = self.curr.pressure

        #serializing method for the class to be converted into a JSON string
    def serializable(self):
        return self.__dict__
