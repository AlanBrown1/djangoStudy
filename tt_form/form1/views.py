from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddForm

# Create your views here.

def index(request):
	if request.method == 'POST':    #当提交表单时
		form = AddForm(request.POST)  #form包含了提交的数据
		if form.is_valid():           #如果提交的数据合法
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			d = int(a) + int(b)*int(c)
			return HttpResponse(str(d))
	else:    #当正常访问时
		form = AddForm()
	return render(request, 'index.html', {'form':form})