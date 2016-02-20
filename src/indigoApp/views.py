from django.shortcuts import render
from django.http import HttpResponse
from getProUsers import ProUsers
from getAssociates import Associates
from getDiyLinks import DiyLinks

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
		pro = ProUsers()
		print selection
		if(selection == 'byProname'):
			proname = request.POST.get('txtProName')
			response = pro.getUserByName('Rala')
			print "Response" +response.CompanyName
		elif(selection == 'byCategory'):
			category = request.POST.get('byCategory')

			response = pro.getUsers('bvCategory', None)
			for user in response:
				print user.CompanyName
				print user.Rating
		print request
	return render(request, 'indigoApp/pro.html')
	
def help(request):
	if request.method == 'POST':
		searchQuery = request.POST.get('answer')
		link = DiyLinks()
		response = link.getDiyLinks('fan')
		print response
		print searchQuery
		print request
	return render(request, 'indigoApp/help.html')
	
def associate(request):
	if request.method == 'POST':
		selection = request.POST.get('selCategory')
		associates = Associates()
		response = associates.getAssociatesFromCategory('Lumber')
		for user in response:
			print user.CompanyName
			print user.Rating
		print selection
	return render(request, 'indigoApp/associate.html')

def demo(request):
	#orm = MyModelForm()
	text = "Hey there" #+ request.POST.get('txtName')
	context = {'response_text': text}
	print request
	return render(request, 'indigoApp/_demo.html', context)

