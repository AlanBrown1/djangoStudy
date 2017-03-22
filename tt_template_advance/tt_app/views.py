from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# reverse的作用是获取网址

# Create your views here.
def home(request):
	s = '今天是2017年3月22日星期三'
	name = ['alan', 'brown','eileen', '我媳妇儿']
	di = {'name':'Alan Brown', 'age':22, 'school':'whu'}
	li = list(range(1,101))
	score = 91
	context_dict = {'s':s, 'name':name, 'info':di, 'li':li, 'score':score}
	return render(request, 'home.html', context_dict)

def add(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def multi(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) * int(b)
	return render(request, 'multiresult.html',{'multiresult':c})

def login(request):
	return render(request, 'login.html')