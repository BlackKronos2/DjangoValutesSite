from django.urls import path, register_converter, include
from django.http import HttpResponseNotFound
from django.views.generic import RedirectView

urlpatterns = [
    path('valutes/', include('valutes.urls')),
    path('blog/', include('valutesBlog.urls')),
    path('', RedirectView.as_view(url='valutes/', permanent=True))
]