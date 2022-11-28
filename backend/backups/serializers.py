from rest_framework import serializers

from .models import Backup

class BackupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='backups:detail-update-drestry',
        lookup_field='pk',
        read_only=True
    )
    class Meta:
        model = Backup
        # fields = '__all__'
        fields = [
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
            'server'
        ]