from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_from_name, {'file_name':'valutesBlog/index'}, name='index'),
]