from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('savedata', views.savedata, name="savedata"),
    path('getdata', views.getdata, name="getdata"),
    path('deletedata/', views.deletedata, name="deletedata"),

]
