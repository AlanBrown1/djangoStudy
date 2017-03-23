from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'home.html')

def plus(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return render(request, 'plus.html', {'plusresult':c})

def multi(request, a, b):
	c = int(a)*int(b)
	return HttpResponse(str(c))
