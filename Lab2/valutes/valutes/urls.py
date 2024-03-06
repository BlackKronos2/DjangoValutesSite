from django.urls import path, register_converter, include
from . import views, converters
from .views import custom_404
from django.http import HttpResponseNotFound

register_converter(converters.YearConverter, 'year')

urlpatterns = [
    path('', views.page_from_name, {'file_name':'valutes/index'}, name='index'),
    path('about_site/', views.page_from_name, {'file_name':'valutes/about_site'}, name='about'),
    path('about_company/', views.page_from_name, {'file_name':'valutes/about_company'}, name='about_site'),
    path('faq/', views.page_from_name, {'file_name':'valutes/FAQ'}, name='FAQ'),

    path('color/<str:color>/', views.color_view),
    path('404/', lambda request: HttpResponseNotFound('Страница не найдена - Ошибка адреса')),

    path('archive/<year:year>/', views.archive_year),
    path('exchange-rate/', views.get_exchange_rate, name='exchange_rate_form'),
    path('current-exchange-rate/', views.current_exchange_rate, name='current_exchange_rate'),

    path('blog/', include('valutesBlog.urls'))
]