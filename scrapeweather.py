import pyowm

owm = pyowm.OWM('bec9f1b7ad458af3371c2ae149d7bb47');
observation = owm.weather_at_place("Ottawa,On");
w = observation.get_weather();
temperature = w.get_temperature('celsius');
tomorrow = pyowm.timeutils.tomorrow();
wind = w.get_wind();



print(w);
print(wind);
print(temperature);
print(tomorrow);
