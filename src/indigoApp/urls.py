from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^demo/', views.demo, name='demo'),
   #url(r'^admin/', admin.site.urls),
    url(r'^$', 'indigoApp.views.index'),
	url(r'^$', views.index2,name='index2'),
    url(r'^$', views.index3,name='index3'),
	url(r'^$', views.index4,name='index4'),
	
]