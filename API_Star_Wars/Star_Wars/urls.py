from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from . import views

router = routers.DefaultRouter()
router.register(r'Person', views.PersonViewSet)
router.register(r'People', views.PeopleViewSet)
router.register(r'Vehicle', views.VehicleViewSet)
router.get_api_root_view().cls.__name__ = "Api Star Wars"
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #path('path/to/my/view/', MySimpleView.as_view())
]  