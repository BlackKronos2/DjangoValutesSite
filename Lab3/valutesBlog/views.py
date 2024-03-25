from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from valutes.models import Currency
from valutesBlog.models import CurrencyArticle

# Create your views here.

def main_page(request):
    displayable_articles = CurrencyArticle.displayable_objects.all()
    currencies = Currency.objects.get_currencies
    return render(request, 'blog_index.html', {'displayable_articles': displayable_articles, 'currencies': currencies})

