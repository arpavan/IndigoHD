from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world!")

def index(request):
#	context = {'sample_text': "Hello World"}
#	return render(request, 'indigoApp/index.html', context)
#    return HttpResponse("Hello, world!")
    return render(request, 'indigoApp/home.html')

def index2(request):
    return render(request, 'indigoApp/firstpage.html')
	
	
def index3(request):
    return render(request, 'indigoApp/help.html')
	
def index4(request):
    return render(request, 'indigoApp/secondpage.html')

def demo(request):
	#orm = MyModelForm()
	text = "Hey there" + request.POST.get('txtName')
	context = {'response_text': text}
	print request
	return render(request, 'indigoApp/demo.html', context)
