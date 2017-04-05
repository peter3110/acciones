from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
	url(r'^getData/$', views.getData, name='getData'),
]

urlpatterns = format_suffix_patterns(urlpatterns)