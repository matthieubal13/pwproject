from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.phenotype_list, name='phenotype_list'),
    url(r'^snp/?$', views.snp_list, name='snp_list'),
    url(r'^(?P<pk>[0-9]+)/?$', views.phenotype_detail,
    name = 'phenotype_detail'),
]
