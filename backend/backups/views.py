from django.shortcuts import render
from rest_framework import generics

from .models import Backup
from .serializers import BackupSerializer


class BackupListCreateAPIView(
    generics.ListCreateAPIView
    ):
    
    queryset = Backup.objects.all()
    serializer_class = BackupSerializer
    
    
class BackupDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
    ):
    
    queryset = Backup.objects.all()
    serializer_class = BackupSerializer