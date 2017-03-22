from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'tt_templates/home.html')