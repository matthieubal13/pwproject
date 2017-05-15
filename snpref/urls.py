from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.phenotype_list, name='phenotype_list'),
    url(r'^(?P<pk>[0-9]+)/?$', views.phenotype_detail,
    name = 'phenotype_detail'),
    url(r'^snp/(?P<pk>[0-9]+)/?$', views.snp_detail,
    name = 'snp_detail'),
]
