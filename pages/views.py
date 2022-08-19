from django.http import HttpResponse
# Create your views here.

def homeview(request):
    return HttpResponse("home page")

def about(request):
    return HttpResponse("about page")
