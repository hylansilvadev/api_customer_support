from rest_framework import viewsets

from .models import Tiket
from .serialeizers import TiketSerialeizer

class TiketViewSet(viewsets.ModelViewSet):
    queryset = Tiket.objects.all()
    serializer_class = TiketSerialeizer