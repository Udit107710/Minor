from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
 #re_path(r'^(?:pl=(?P<petal_length>?([0-9]*[.])?[0-9]+)&pw=(?P<petal_width>?([0-9]*[.])?[0-9]+)&sl=(?P<sepal_length>?([0-9]*[.])?[0-9]+)&sw=(?P<sepal_width>?([0-9]*[.])?[0-9]+)/', views.predict),
 #re_path(r'pl=(?P<petal_length>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+))/pw=(?P<petal_width>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+))/sl=(?P<sepal_length>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+))/sw=(?P<sepal_width>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+))/', views.predict),

 #re_path(r'^(?:pl=(?P<petal_length>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)))&(?:pw=(?P<petal_width>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)))&(?:sl=(?P<sepal_length>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)))&(?:sw=(?P<sepal_width>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)))/?$', views.predict),
 path('predict/', views.predict),

]
