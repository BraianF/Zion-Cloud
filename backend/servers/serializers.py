from .models import Server
from rest_framework import serializers


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='servers:detail-update-drestry',
        lookup_field='pk',
        read_only=True
    )
    class Meta:
        model = Server
        fields = [
            'url', 
            'hostname',
            'description',
            'ip_address',
            'ssh_user',
            'ssh_port',
            'token',
            'created',
            'updated',
            'active',
            'customer'
        ]