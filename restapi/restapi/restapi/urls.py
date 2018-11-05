from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'videos', views.VideoViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# print(rest_framework.urls)
urlpatterns = [
    url(r'^your_name$', views.get_name, name='your_name'),
    url(r'^thanks$', views.thanks, name='thanks'),
    url(r'^contactUs', views.contactUs, name='contactUs'),
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
