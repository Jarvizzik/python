from django.urls import path,re_path  
from . import views

urlpatterns = [
    path('',views.start, name="start"),
    path('register',views.register, name="register"),
    path('index',views.index, name="index"),
    path('add',views.add),
    re_path(r'^edit/(?P<id>\d+)$', views.edit),
    re_path(r'^update/(?P<id>\d+)$', views.update),
    re_path(r'^delete/(?P<id>\d+)$', views.destroy)
]
