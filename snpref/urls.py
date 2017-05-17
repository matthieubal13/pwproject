from django.conf.urls import url
from . import views

# Description of the differents URLs to do the connection with the views
urlpatterns = [
    url(r'^$', views.phenotype_list, name='phenotype_list'),
    url(r'^snp/?$', views.snp_list, name='snp_list'),
    url(r'^(?P<pk>[0-9]+)/?$', views.phenotype_detail,
    name = 'phenotype_detail'),
    url(r'^snp/(?P<pk>[0-9]+)/?$', views.snp_detail,
    name = 'snp_detail'),
    url(r'^search/$', views.snp_search,
    name = 'search'),
]
