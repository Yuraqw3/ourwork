from django.urls import path , include
from django.contrib import admin

urlpatterns = [
    path('', include('base.urls')),
    path('admin/',admin.site.urls)
]
