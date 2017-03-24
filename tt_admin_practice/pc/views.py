from django.shortcuts import render
from django.http import HttpResponse

from .models import Computer as com, Book as bo
# Create your views here.

def home(request):
	return render(request, 'home.html')

def computer(request):
	com_list = list(com.objects.values('name','master','brand','price'))
	return render(request, 'computer.html', {'li':com_list})

def book(request):
	bo_list = list(bo.objects.values('name', 'author', 'price', 'status'))
	return render(request, 'book.html', {'li': bo_list})