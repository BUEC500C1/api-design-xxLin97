import requests
import csv


def get_city_name(airport_name):
    with open("airports.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[3] == airport_name:
                return row[10]
    return ""

def get_data(city):
  API_KEY = ''
  basic_url = 'http://api.openweathermap.org/data/2.5/weather?'
  url = basic_url + "&q=" + city + "&appid=" + API_KEY
  res = requests.get(url)
  data = res.json()
  return data


def show_information(data):
  if data["cod"] != "400":
    temp = data['main']['temp']
    feels_like = data["main"]["feels_like"]
    wind_speed = data['wind']['speed']
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    description = data['weather'][0]['description']
    print('Temperature :' +temp + 'degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Humidity : {}%'.format(humidity))
    print('Description : {}'.format(description))
  else:
    print("Wrong airport name")


def main():
    airport_name = input ("Enter the name of the Airport: ")
    city = get_city_name(airport_name)
    data = get_data(city)
    show(data)


if __name__ == '__main__':
  main()