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
 # django can auto matically figure out the base name by
 #the model thats register with the serializer on the view set
router.register('profile', views.UserProfileViewSet)
#its not  a model view set so we need the base_name
router.register('login', views.LoginViewSet, base_name='login')
urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    #router create the url for us automatically generate
    url(r'', include(router.urls))
]
