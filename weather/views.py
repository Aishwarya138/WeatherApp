from django.shortcuts import render
# When we send request to the api we get the response in the json format so we import it
import json
import urllib.request

# Create your views here.
def home(request):
  if request.method == 'POST':
    city = request.POST['city']
    # appid=<API Key>
    res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1d12539417fa770d08669d6565f00d04').read()
    json_data = json.loads(res)
    data = {
      "country_code": str(json_data['sys']['country']),
      "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
      "temp": str(json_data['main']['temp']) + 'k',
      "pressure": str(json_data['main']['pressure']),
      "humidity": str(json_data['main']['humidity']),
    }
  else:
    city = ''
    data = {}
  return render(request, 'home.html', {'city': city, 'data': data})