from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.dbprocessing),
    path('insert/',views.insertemployee,name="inserturl"),
    path('select/<int:pno>/',views.selectemployee,name="selecturl"),
    path('update/<int:eno>/',views.updateemployee,name="updateurl"),
    path('delete/<int:eno>/',views.deleteemployee,name="deleteurl"),
    path('detail/<int:eno>/',views.detailemployee,name="detailurl"),
    path('login/',views.loginpage,name='loginurl'),
    path('logout/',views.logoutpage,name='logouturl'),
    path('register/',views.registerpage,name='registerurl'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

