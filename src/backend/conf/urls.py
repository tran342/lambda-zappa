from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from api.resource import RiskTypeViewSet

router = DefaultRouter()
router.register(r'risk-types', RiskTypeViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
