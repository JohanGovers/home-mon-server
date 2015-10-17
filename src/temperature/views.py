from django.shortcuts import render
from django.http import HttpResponse
from temperature.models import TempReading

def index(request):
    return HttpResponse("Hello, world. You're at the home-mon-server index page.")

def save_temp_reading(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        date = request.POST.get('date')

        entry, created = TempReading.objects.create(value=value, date=date)
        entry.save()

        response_data = {}
        response_data['msg'] = 'Added new entry with value set to ' + str(value)

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse()
