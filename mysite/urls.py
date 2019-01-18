from django.conf import settings

from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic import TemplateView

from django.contrib import admin
from mysite import views

urlpatterns = [
    url("", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url('notifications/', include('django_nyt.urls')),
    url("account/", include("account.urls")),

    url("dashboard/", TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
    url("aboutus/", TemplateView.as_view(template_name="aboutus.html"), name="aboutus"),
    url("forms/form1", TemplateView.as_view(template_name="forms/form1.html"), name="form"),
    url("forms/form2", TemplateView.as_view(template_name="forms/form2.html"), name="form2"),
    #url('forum/', include(board.urls)),
    url(r'form', views.MyView, name="form"),
    url(r'articles', include('blog.urls')),
    url('profile', TemplateView.as_view(template_name="profile/profile.html"), name="profile"),
    url('hub', TemplateView.as_view(template_name="hub.html"), name="hub"),

    url('events', TemplateView.as_view(template_name="events.html"), name="events"),
    url(r"messages/", include("pinax.messages.urls", namespace="pinax_messages")),
    url(r'wiki/', include('wiki.urls')),
    url(r'friendship/', include('friendship.urls')),
    # View URLs
    url('fobi/', include('fobi.urls.view')),

    # Edit URLs
    url('fobi/', include('fobi.urls.edit')),
    url(r'fobi/plugins/form-handlers/db-store/',
    include('fobi.contrib.plugins.form_handlers.db_store.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
