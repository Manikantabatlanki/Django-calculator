from django.urls import path
from .import views
urlpatterns=[
    path('',views.Accfun),
    path('',views.Acc2fun)
]