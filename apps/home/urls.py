from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import *

urlpatterns = patterns('apps.home.views',
	url(regex=r'^$',
		view= TemplateView.as_view(template_name="home/index.html"),
    	name='index'
    	),
	url(regex=r'^persona/$',
		view= PersonaCreateView.as_view(),
    	name='add_persona'
    	),
	url(regex=r'^save_image/(?P<cedula>\d+)/$',
	 	view=SaveImage.as_view(),
	 	name='salvar_imagen'
	 	),
	url(regex=r'^persona/(?P<pk>\d+)/$',
	 	view=PersonaView.as_view(),
	 	name='persona'
	 	),
	url(regex=r'^persona/list/$',
	 	view=PersonaList.as_view(),
	 	name='persona_list'
	 	),
	url(regex=r'^contacto/$',
	 	view=TemplateView.as_view(template_name="home/contacto.html"),
	 	name='contacto'
	 	),
)
