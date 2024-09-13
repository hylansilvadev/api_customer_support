from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from tiket.views import TiketViewSet
from user.views import UserViewSet


router = DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"tiket", TiketViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
