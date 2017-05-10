from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.phenotype_list, name='phenotype_list'),
]
