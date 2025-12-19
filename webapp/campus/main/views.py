from django.http import HttpResponse

def home(request):
    return HttpResponse("Smart Campus Django is running")