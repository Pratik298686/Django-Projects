from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
import requests
import datetime

# Create your views here.

def index(request):
    # if request.method == 'POST':
    #     city = request.POST['city']

    #     # source contain json data from api
    #     source = urllib.request.urlopen(
    #         'https://api.openweathermap.org/data/2.5/weather?q={Mumbai}&appid={key 1e6b176625ebe3adb848d0d1610ce655}').read()
    #     # converting json data to dictionary
    #     list_of_data = json.loads(source)
        

    #     # data for variable list_of_data
    #     data = {
    #         "country_code": str(list_of_data['sys']['country']),
    #         "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
    #         "temp": str(list_of_data['main']['temp']) + 'k',
    #         "pressure": str(list_of_data['main']['pressure']),
    #         "humidity": str(list_of_data['main']['humidity']),
    #     }
    #     print(data)

        
    # else:
    #     data = {}
    # return render(request, 'main/index.html',data)
    city = ''
    if request.method == 'POST':
        city = request.POST['city']
    else:
        city = "Mumbai"
    
    appid = '1e6b176625ebe3adb848d0d1610ce655'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()

    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']

    day = datetime.date.today()


    return render(request, 'main/index.html',{'description':description,'day':day,'temp':temp, 'icon':icon, 'city':city})
    
