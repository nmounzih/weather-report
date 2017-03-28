# import requests
# import requests_mock
from weather_classes import Current_conditions
import json

# with requests_mock.Mocker() as m:
#     m.get('http://api.wunderground.com/api/b042b9ca2dcb4435/alerts/currenthurricane/forecast10day/astronomy/conditions/q/27703', text='resp')
#     requests.get('http://api.wunderground.com/api/b042b9ca2dcb4435/alerts/currenthurricane/forecast10day/astronomy/conditions/q/27703').text

with open('report.json', 'r') as f:
    data = json.load(f)


def test_current_conditions():
    c = Current_conditions(data)
    assert c.set(['current_observation']['display_location']['full']) == "Durham, NC"
