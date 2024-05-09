from django.contrib import admin
from django.urls import path
from .home import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
]
