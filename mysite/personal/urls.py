from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^personal/$', views.index, name="index"),
    url(r'^personal/contact/$', views.contact, name="contact"),
]
