from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.connection, name='connection'),
    url(r'^disconnection/?$', views.disconnection, name='disconnection'),
]
