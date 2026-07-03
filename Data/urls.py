from django.urls import path
from .import views
urlpatterns=[
    path('',views.dataprocess),
    path('insert/',views.insertemployee,name='inserturl'),
    path('select/<int:pno>/',views.selectemployee,name='selecturl'),
    path('update/<int:eid>/',views.updateemployee,name='updateurl'),
    path('delete/<int:eid>/',views.deleteemployee,name='deleteurl'),
    path('login/',views.loginpage,name='loginurl'),
    path('logout/',views.logoutpage,name='logouturl'),
    path('register/',views.registerpage,name='registerurl'),
]
 