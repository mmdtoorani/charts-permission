from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from main.api.serializer import StaffListSerializer, ChartListSerializer
from main.models import ChartModel


class StaffListAPIView(APIView):
    def get_queryset(self):
        """Returns all users who are staff"""
        return User.objects.filter(is_staff=True)

    def get(self, request):
        queryset = self.get_queryset()
        serializer = StaffListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class ChartAPIView(APIView):
    def get_queryset(self):
        """Returns all Charts"""
        return ChartModel.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = ChartListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)
