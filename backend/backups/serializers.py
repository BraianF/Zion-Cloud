from rest_framework import serializers

from .models import Backup
from servers.models import Server

class BackupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='backups:detail-update-drestry',
        lookup_field='pk',
        read_only=True
    )
    server = serializers.HyperlinkedRelatedField(queryset=Server.objects.all(), view_name='servers:detail-update-destroy')
    server_name = serializers.CharField(source='server', read_only=True)
    class Meta:
        model = Backup
        # fields = '__all__'
        fields = [
            'pk',
            'url',
            'description',
            'daily_retention',
            'monthly_retention',
            'yearly_retention',
            'logs_retention',
            'source_folders',
            'additional_parameters',
            'report_address',
            'created',
            'updated',
            'active',
            'server',
            'server_name',
        ]