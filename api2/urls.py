from django.urls import path
from .import views
urlpatterns=[
    path('getemployees/',views.EmployeApiView.as_view()),
    path('update/<int:eno>/',views.updateapi),
    path('custom/',views.CustomApi),
]