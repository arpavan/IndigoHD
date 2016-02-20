from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
	url(r'^demo/', views.demo, name='demo'),
    url(r'^pro/', views.pro,name='pro'),
    url(r'^assoc/', views.associate,name='associate'),
	url(r'^help/', views.help,name='help'),
	
]