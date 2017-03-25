from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
	return render(request, 'home.html')

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	if a == '':
		a = 0
	if b == '':
		b = 0
	c = int(a) + int(b)
	return HttpResponse(str(c))

def ajax_list(request):
	li = list(range(1,11))
	return JsonResponse(li, safe=False)

def ajax_dict(request):
	di = {'name':'tongting', 'age':22, 'school':'whu','num':'2016202130012'}
	return JsonResponse(di)