from django.http import HttpResponse
from . import tasks

def home(request):
    tasks.download_cat.delay()
    return HttpResponse('<h1>Loading</h1>')

# Create your views here.
