import requests
from django.shortcuts import render


def covid19_API(n):
    URL = 'http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/'+str(n)+'/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data


def home(request):
    value = covid19_API(1)[0]
    year = covid19_API(365)
    year_data = []

    for data in year:
        date = data['S_DT']
        confirmed = data['N_HJ']
        year_data.append([date, int(confirmed)])
    week_data = year_data[:7]
    week_data.reverse()
    year_data.reverse()
    return render(request, 'home.html', {'value': value, 'week_data': week_data, 'year_data':year_data})
