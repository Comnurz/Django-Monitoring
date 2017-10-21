from django.shortcuts import render

# Create your views here.
def index(request):
    values= [['foo', 32], ['bar', 64], ['baz', 96]]
    return render(request, 'monitor/index.html', {'values': values})

def data(request):

    return render(request, 'monitor/index.html',{'values':values})
