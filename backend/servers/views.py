from rest_framework import generics

from .models import Server
from .serializers import ServerSerializer


class ServerListCreateAPIView(
    generics.ListCreateAPIView
    ):
    
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    
    
class ServerDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
    ):
    
    queryset = Server.objects.all()
    serializer_class = ServerSerializer