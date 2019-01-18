from django.conf.urls import url, include
from django.views.generic import ListView, DetailView,UpdateView
from .models import blogpost
from blog import views

urlpatterns = [url(r'^$',ListView.as_view(queryset=blogpost.objects.all().order_by("-date")[:25],template_name="blog.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model=blogpost,template_name="blog_post.html")),
                url(r'^(?P<pk>\d+)/edit/$', views.editpost,name="EditPost")

               ]