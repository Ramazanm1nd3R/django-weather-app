import requests
from django.shortcuts import render

def get_weather(request):
    api_key = "weather_token"
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city')
        if not city:
            error_message = "Поле не может быть пустым, попробуйте снова."
        else:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = "Проверьте корректность названия города и попробуйте снова."

    return render(request, 'weather_app/weather.html', {'weather_data': weather_data, 'error_message': error_message})
