from rest_framework import viewsets

from user.models import User
from user.serialeizers import UserSerialeizer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialeizer
