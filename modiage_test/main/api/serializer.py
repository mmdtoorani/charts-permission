from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import ChartModel


class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # exclude_fields = ('password',)


class ChartListSerializer(serializers.ModelSerializer):
    staff = serializers.ReadOnlyField(
        source='staff_username',
        read_only=True,
    )

    class Meta:
        model = ChartModel
        fields = '__all__'
