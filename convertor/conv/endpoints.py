from django.conf.urls import url

from . import api

urlpatterns = [
    url("convert/url/$", api.ConverterUrlAPI.as_view()),
    url("convert/file/$", api.ConverterFileAPI.as_view()),
]
