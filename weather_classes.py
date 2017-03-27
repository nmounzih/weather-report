

class Current_conditions:

    def __init__(self, report):
        self.city_and_state = report['current_observation']['display_location']['full']
        self.weather = report['current_observation']['weather']
        self.temp_f = report['current_observation']['temp_f']
        self.humidity = report['current_observation']['relative_humidity']
        self.wind = report['current_observation']['wind_mph']

    def __repr__(self):
        return "Location: {}\nWeather: {}\nTemperature(F): {}\nHumidity: {}\nWind Speed: {}".format(self.city_and_state, self.weather, self.temp_f, self.humidity, self.wind)


class Sunrise_set:

    def __init__(self, report):
        self.sunrise = report['moon_phase']['sunrise']
        self.sunset = report['moon_phase']['sunset']

    def __repr__(self):
        return "Sunrise: {}\nSunset: {}".format(self.sunrise, self.sunset)


class Hurricane:

    def __init__(self, report):
        self.name = report['currenthurricane']


    def __repr__(self):
        if self.name:
            hurricanes = []
            for hurricane in self.name:
                hurricanes.append(hurricane['stormInfo']['stormName_Nice'])
            return "Hurricane found (could be anywhere): {}".format(hurricanes)
        else:
            return "There are no current hurricanes."


class Alert:

    def __init__(self, report):
        self.name = report['alerts']


    def __repr__(self):
        if self.name:
            return "ALERT!!!"
        else:
            return "No alerts."


class TenDay:

    def __init__(self, report):
        self.forecast = report['forecast']['txt_forecast']['forecastday']

    def __repr__(self):
        day_list = []
        for day in self.forecast:
            day_list.append((day['title'], day['fcttext']))
        empty_string = ""
        for item in day_list:
                empty_string += "{}:{}\n\n".format(item[0], item[1])
        return "Ten Day Forecast: {}\n".format(empty_string)
