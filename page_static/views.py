from django.shortcuts import render
from django.http import HttResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>entre em contato <br> (21)965084996 <br> ricardosholna@gmail.com </h1>")