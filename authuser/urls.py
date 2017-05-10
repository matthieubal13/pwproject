from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
]
