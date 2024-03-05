from django.urls import path, register_converter, include
from . import views, converters
from .views import custom_404
from django.http import HttpResponseNotFound

register_converter(converters.YearConverter, 'year')

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.dynamic, name='dynamic'),
    path('color/<str:color>/', views.color_view),
    path('404/', lambda request: HttpResponseNotFound('Страница не найдена - Ошибка адреса')),
    path('archive/<year:year>/', views.archive_year),
    path('exchange-rate/', views.get_exchange_rate, name='exchange_rate_form'),
    path('current-exchange-rate/', views.current_exchange_rate, name='current_exchange_rate'),

    path('blog/', include('valutesBlog.urls'))
]