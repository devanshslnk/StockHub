from django.conf.urls import url
from . import  views
from .views import *
urlpatterns=[
    url(r'^$',views.login_site,name='login'),
    url(r'^logout/$',views.logout_site,name='logout'),
    url(r'^register/$',views.register_user,name='register'),



]