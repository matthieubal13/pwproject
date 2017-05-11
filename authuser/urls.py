from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.connexion, name='connection'),
    url(r'^disconnection/?$', views.deconnexion, name='disconnection'),
]
