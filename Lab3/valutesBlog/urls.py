from django.urls import path
from . import views

app_name = "valutesBlog"

urlpatterns = [
    path('', views.main_page, name='blog_index'),
]