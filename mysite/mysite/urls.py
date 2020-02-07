from django.contrib import admin
from django.urls import include, path
# from django.http import HttpResponse
from django.shortcuts import render


def landingpage(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', landingpage, name='landing'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
