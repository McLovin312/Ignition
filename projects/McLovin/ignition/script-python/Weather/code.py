# Weather Scripts
# to test run Weather.generateWeeklyForecasts() in Script Console and check tags in [default]Ignition/Forecasts and/or the Output Console for errors

def generateWeeklyForecasts():
	# run the weekly forecast script for all locations
	locations = getLocations()
	# write the forecast data to memory tags for access
	for location in locations:
		lat = location["lat"]
		long = location["long"]
		name = location["name"]
		system.tag.writeBlocking(["[default]Ignition/Forecasts/"+str(name)], [weeklyForecast(lat,long,name)])
		
def getLocations():
	# return dataset of locations (list of dictionaries)
	query = "SELECT * FROM locations"
	return system.db.runPrepQuery(query)

def weeklyForecast(lat, long, name):
	# create logger for errors
	logger = system.util.getLogger("WeatherScripts")
	# create HTTP Client Object
	client = system.net.httpClient()
	# format lat and long as 4 decimal numbers, then convert to strings
	lat = str(round(lat, 4))
	long = str(round(long, 4))
	# format first endpoint URL for fetching the actual Forecast endpoint(s) for location (based on lat/long)
	URL = "https://api.weather.gov/points/"+lat+","+long
	# no headers are needed in this example, but many APIs would require some specific format here
	headers = {}
	# run a GET request to the weather.gov API to find the forecast URLs
	response = client.get(URL, headers = headers)
	# if the response is good continue with forecast request
	if response.getStatusCode() == 200:
		# once a valid response is recieved, interact with the response object
		responseData = system.util.jsonDecode(response.getText())
		# if API endpoint for the forecast exists, call it below
		if responseData["properties"]["forecast"]:
			# run a GET request against the local forecast weather by providing the API URL from the inital request
			forecast = client.get(responseData["properties"]["forecast"], headers = headers)
			# extract the raw forecast JSON text into a python Object
			forecastData =  system.util.jsonDecode(forecast.getText())
			# check that the return forecast type isn't the APIs "UnexpectedProblem" return
			if forecastData["type"] == "https://api.weather.gov/problems/UnexpectedProblem":
				# prints error related to API unexpected errors
				logger.info("API Likely Down Temporarily in Area. "+str(name))
				return -1
			else:
				# extract useful values from the forecast
				generatedAt = forecastData["properties"]["generatedAt"] #time request was generated at
				periods = forecastData["properties"]["periods"] #actual forecast data
				
				# create list of forecast objects to store
				instances = []
				# for each view, provide the parameters expected in a dictionary named "data"
				# review the params on the Weather/Embedded Views to see values being returned for the forecast periods
				for value in periods:
					instances.append({"data":value})
				# return the creates list of forecast object instances
				logger.info("Returned Good Forecast Data. "+str(name))
				return instances
		else:
			# prints generic error if response data doesn't include expected Forecast API endpoint URLs
			logger.info("No Forecast of Expected Format. "+str(name))
			return -1
	else:
		# prints generic error if initial response request is bad
		logger.info("Bad Status for latitude and longitude points to weather.gov. "+str(name))
		return -1