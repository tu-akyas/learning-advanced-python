import requests, pprint


# city1 = "Chennai"
# apikey1 = "secret"
# url1 = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}"
# url2 = "api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}"
# r1 = requests.get(url1)
# print(r.json())


class Weather:
    """Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates
    Package use example:
    # create a weather object using city name:
    # The api key below is dummy value,
    # Get your own apikey from https://openweathermap.org
    # And wait for few hours as it takes sometime to activate the apikey

    >>> weather1 = Weather(apikey="Get your own api key", city="Seattle")

    # Using lattitude and longitude coordinates
    >>> weather2 = Weather(apikey="Get your own api key", lat=41.1, lon=-4.1)

    # Get complete weather data for the next 12 hours:
    >>> weather1.next12h()

    # Simplified data for the next 12 hours:
    >>> weather1.next_12h_simplified()

    """

    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments")

        if self.data['cod'] != '200':
            raise ValueError(self.data["message"])

    def next_12h(self):
        """Returns 3 hour data for the next 12 hours as a dict"""
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """Returns 3 hour data for the next 12 is a simplified format"""
        simplified_data = []
        for data_list in self.data['list'][:4]:
            simplified_data.append((
                data_list['dt_txt'],
                data_list['main']['temp'],
                data_list['weather'][0]['description']
            ))
        return simplified_data


if __name__ == "__main__":
    apikey = "get your own secret key"
    weather = Weather(apikey=apikey, city="Hongkong")
    pprint.pprint(weather.next_12h())
    pprint.pprint(weather.next_12h_simplified())
