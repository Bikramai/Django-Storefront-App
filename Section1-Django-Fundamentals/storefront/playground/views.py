from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# request -> response
# reequest handler
# action
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Bikram'})