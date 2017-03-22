from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
	return render(request, 'home.html')

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def multi(request, a, b, c):
	d = int(a)*int(b)*int(c)
	return HttpResponse(str(d)+'网址：'+ reverse('multi', args=(a,b,c)))

def old_multi(request, a, b, c):
	return HttpResponseRedirect(reverse('multi', args=(a,b,c)))
