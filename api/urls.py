from django .urls import path
from .import views
urlpatterns=[
    path('getemployees/',views.getemployees),
    path('update/<int:eno>/',views.update),
    path('deleteemployees/<int:eno>/',views.delete)
]