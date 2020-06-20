import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
# print(json_data.json())

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar",
                    "rate":7.0822331710729e-5,"date":"Fri, 19 Jun 2020 12:00:01 GMT","inverseRate":14119.840110383},

             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro",
                    "rate":6.3139633186564e-5,"date":"Fri, 19 Jun 2020 12:00:01 GMT","inverseRate":15837.912726626}}
# print(json_data)
for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])

