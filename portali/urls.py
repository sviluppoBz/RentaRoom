from django.conf.urls import url
from .import views

urlpatterns	=[
	url(r'^$',views.listaPortali,name='listaPortali'),
	url(r'^portali/(?P<pk>[0-9]+)/$', views.ilPortale, name='ilPortale'), 	
	url(r'^portali/nuovoPortale/$',	views.nuovoPortale,	name='nuovoPortale'),
	url(r'^portali/(?P<pk>[0-9]+)/modiPortale/$',	views.modiPortale, name='modiPortale'),
]