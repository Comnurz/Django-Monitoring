from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    values= []
    r = requests.get('http://localhost:8080/data')
    res=r.json()
    for key, value in res.items():
    	values.append(['total ram',value[0][1]])
    	values.append(['used ram',value[1][1]])
    	#values.append(['Disk',value[2][1]])
    return render(request, 'monitor/index.html', {'values': values})

