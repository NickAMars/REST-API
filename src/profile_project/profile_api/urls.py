from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(
'hello-viewset', #name of or api
 views.HelloViewSet, # name of viewset
 base_name='hello-viewset'
 )

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    #router create the url for us automatically generate
    url(r'', include(router.urls))
]
