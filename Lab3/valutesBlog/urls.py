from django.urls import path
from . import views

app_name = "valutesBlog"

urlpatterns = [
    path('', views.page_from_name, {'file_name': 'blog_index'}, name='blog_index'),
]