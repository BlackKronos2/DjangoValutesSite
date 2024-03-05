from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'valutesBlog/index.html')
