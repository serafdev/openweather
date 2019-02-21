import configparser
import requests
import sys


class Config:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('api_key.ini')
        self.api_key = config['OpenWeather']['Key']


class Weather:

    def __init__(self):
        self.api_key = Config().api_key
        
    def get(self, location='montreal'):
        req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=montreal,ca&APPID={self.api_key}')
        return req.content


def main():
    assert len(sys.argv) >= 2, 'Please enter a command'
    weather = Weather()
    print(weather.get(sys.argv[1]))


if __name__ == '__main__':
    main()


