from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^top/', views.top_twenty, name='top_twenty'),
    url(r'^users/', views.users, name='users'),
]
