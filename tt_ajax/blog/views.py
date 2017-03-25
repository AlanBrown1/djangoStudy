from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
	return render(request, 'home.html')

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def ajax_list(request):
	a = list(range(100))
	return 	JsonResponse(a, safe=False)

def ajax_dict(request):
	name_dict = {'tong': 'Love python and Django', 'ting': 'I am teaching Django'}
	return JsonResponse(name_dict)