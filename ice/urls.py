from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^north/', views.north, name='north'),
    url(r'^south/', views.south, name='south'),
    url(r'^$', views.index, name='index'),
]
