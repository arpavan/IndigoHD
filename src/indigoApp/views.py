from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	context = {'sample_text': "Hello World"}
	return render(request, 'indigoApp/index.html', context)
#    return HttpResponse("Hello, world!")

#def demo(request):
#	context = {'response_text': request.
#	return render(request, 'indigoApp/demo.html', context)