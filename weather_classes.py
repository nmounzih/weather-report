import requests


class Current_conditions:

    def __init__(self):
        zipcode = input("Enter zipcode: ")
        r = requests.get('http://api.wunderground.com/api/b042b9ca2dcb4435/alerts/current_hurricane/forecast10day/astronomy/conditions/q/{}.json'.format(zipcode))
        json_dict = r.json()
        self.city_and_state = json_dict['current_observation']['display_location']['full']
        self.weather = json_dict['current_observation']['weather']
        self.temp_f = json_dict['current_observation']['temp_f']
        self.humidity = json_dict['current_observation']['relative_humidity']
        self.wind = json_dict['current_observation']['wind_mph']


    def __repr__(self):
        return "Location: {}/n"
