from django.conf import settings as original_settings
 
 
def settings(request):
    return {'settings': original_settings}
 
 
def ip_address(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def book(request):
	return {'what': 'there are some books.'}

def current_path(request):
	return {'path': request.path }

def user_info(request):
	return {'username':'Alan Brown', 'age':22 }