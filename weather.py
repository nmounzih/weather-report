import requests
from weather_classes import Current_conditions, Sunrise_set, Hurricane, Alert, TenDay


def main():
    zipcode = input("Enter zipcode: ")
    r = requests.get('http://api.wunderground.com/api/b042b9ca2dcb4435/alerts/currenthurricane/forecast10day/astronomy/conditions/q/{}.json'.format(zipcode))
    report = r.json()
    print(Current_conditions(report))
    print(Sunrise_set(report))
    print(Hurricane(report))
    print(Alert(report))
    print(TenDay(report))


if __name__ == '__main__':
    main()
