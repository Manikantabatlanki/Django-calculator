from django.urls import path
from .import views
urlpatterns=[
    path('first/',views.firstform),
    path('insert/',views.insertemployee)
]