from django.conf.urls import url
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^home/$',views.home,name='home'),
    url(r'^ownersite/$',views.owner,name='owner'),
    url(r'^search/$',views.search,name='search'),
    url(r'^admin_site',views.admin_site,name="admin_site")


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)