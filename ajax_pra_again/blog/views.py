from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
	return render(request, 'home.html')

def login(request):
	username = request.GET['username']
	pwd = request.GET['pwd']
	if username == 'tong' and pwd == '123456':
		res = '登录成功'
	else:
		res = '用户名或密码错误'
	return HttpResponse(res)

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
	li = ['i', 'love', 'you', 'so', 'much']
	return JsonResponse(li, safe=False)

def ajax_dict(request):
	di = {'name':'Alan Brown', 'age':23, 'school':'whu'}
	return JsonResponse(di)