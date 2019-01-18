from django.conf.urls import url, include
from django.contrib import admin
#from wagtail.admin import urls as wagtailadmin_urls
#from wagtail.core import urls as wagtail_urls
#from wagtail.documents import urls as wagtaildocs_urls
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from search import views as search_views
from .import views

urlpatterns = [
 #   url(r'^admins/', include(wagtailadmin_urls)),
    #url(r'^documents/', include(wagtaildocs_urls)),

    url('binary/', search_views.search, name='search'),
    url('dashboard/', views.dashboard, name='dashboard'),
    url('link/', views.link, name='link'),
    url("contact/", views.contact, name="contact"),
    # url("edit/", views.edit, name="edit"),
    # url("update/", views.update, name="update"),
    url("update_password/", views.update_password, name="update_password"),
    url("hub/", views.hub, name="hub"),

    url("user_profile/", views.user_profile, name="user_profile"),
    url("terms/", views.basic, name="basic"),
    url("edit_info/", views.edit_info, name="edit_info"),
    url("update_basic_info/", views.update_basic_info, name="update_basic_info"),
    url("update_photo/", views.update_photo, name="update_photo"),
    url("edit_photo/", views.edit_photo, name="edit_photo"),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
   # url(r'', include(wagtail_urls)),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

