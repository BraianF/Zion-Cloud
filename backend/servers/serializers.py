from .models import Server
from customers.models import Customer
from rest_framework import serializers


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='servers:detail-update-destroy',
        lookup_field='pk',
        read_only=True
    )
    customer = serializers.HyperlinkedRelatedField(queryset=Customer.objects.all(), view_name='customers:detail-update-destroy')
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