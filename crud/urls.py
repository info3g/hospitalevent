from django.conf.urls import url
from .import views

urlpatterns = [
    url('register/', views.signup, name='signup'),
    url('book/', views.I_am_going, name='I_am_going'),
    url('signin/', views.signin, name='signin'),

    url('forget/', views.forget, name='forget'),
    url("logout/", views.pagelogout, name="pagelogout"),
    url("basic/", views.basic, name="basic"),
    url("basic_list/", views.basic_list, name="basic_list"),

    url('reset-password/', views.reset_password, name='reset_password'),

    url('event_list_admin/', views.event_list_admin, name='views.event_list_admin'),
]