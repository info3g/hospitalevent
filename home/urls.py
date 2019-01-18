from django.conf.urls import url
from . import views
urlpatterns = [
    url('list/', views.index, name='index'),
    url('thanks/', views.thanks, name='thanks'),
    url('event/', views.event, name='event'),
]