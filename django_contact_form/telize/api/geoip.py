import requests


class Geoip():
    def get(self):
        response = requests.get('http://www.telize.com/geoip')

        return response.json()
