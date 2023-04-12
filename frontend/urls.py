from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('log', views.log, name="log"),
    path('chart', views.chart, name="chart"),
    path('aboutus/', views.about_us, name="amongus"),
    path('login', views.loginview, name="login"),
    path('logout', views.logoutview, name="logout"),
]
