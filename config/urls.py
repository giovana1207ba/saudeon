from django.urls import path
from app.views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('sobre/', sobre, name='sobre'),
    path('register/', register, name='register'),
    path('consulta/', ConsultaView.as_view(), name='consulta')
]
