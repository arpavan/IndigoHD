from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world!")

def index(request):
#	context = {'sample_text': "Hello World"}
#	return render(request, 'indigoApp/index.html', context)
#   return HttpResponse("Hello, world!")
    return render(request, 'indigoApp/index.html')

def pro(request):
	#if request type is POST, process data
	if request.method == 'POST':
		selection = request.POST.get('byCategory')
		if(selection == 'byProname'):
			proname = request.POST.get('txtProName')
#			SQL query
		elif(selection == 'byCategory'):
			category = request.POST.get('optCategory')
#			SQL query
		print request
	return render(request, 'indigoApp/pro.html')
	
def help(request):
	if request.method == 'POST':
		searchQuery = request.POST.get('optCategory')
#		SQL query
		print request
	return render(request, 'indigoApp/help.html')
	
def associate(request):
	if request.method == 'POST':
		selection = request.POST.get('byCategory')
		if(selection == 'byProname'):
			proname = request.POST.get('txtProName')
#			SQL query
		elif(selection == 'byCategory'):
			category = request.POST.get('optCategory')
#			SQL query
		print request
	return render(request, 'indigoApp/associate.html')

def demo(request):
	#orm = MyModelForm()
	text = "Hey there" #+ request.POST.get('txtName')
	context = {'response_text': text}
	print request
	return render(request, 'indigoApp/_demo.html', context)

