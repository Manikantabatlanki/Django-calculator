from django.urls import path
from .import views
urlpatterns=[
    path('add/',views.Calculator.as_view()),
    path('multi/',views.Calculator2.as_view()),
    path('insert/',views.InsertView.as_view()),
    path('update/<int:pk>/',views.ModifyView.as_view()),
    path('select/',views.SelectView.as_view()),
    path('delete/<int:pk>/',views.DeleteView.as_view()),

]