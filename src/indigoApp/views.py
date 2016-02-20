from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world!")

def index(request):
    return render(request, 'indigoApp/home.html')

def index2(request):
    return render(request, 'indigoApp/firstpage.html')
	
	
def index3(request):
    return render(request, 'indigoApp/help.html')
	
def index4(request):
    return render(request, 'indigoApp/secondpage.html')