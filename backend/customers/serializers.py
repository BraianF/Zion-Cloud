from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='customers:detail-update-drestry',
        lookup_field='pk',
        read_only=True
    )
    class Meta:
        model = Customer
        # fields = '__all__'
        fields = [
            'url', 
            'razao_social', 
            'nome_fantasia', 
            'inscricao_federal',
            'phone', 
            'email', 
            'created', 
            'updated', 
            'active'
        ]