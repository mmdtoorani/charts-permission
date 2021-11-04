from django.urls import path

from .views import StaffListAPIView, ChartAPIView

urlpatterns = [
    path('staff_list/', StaffListAPIView.as_view(), name='staff_list'),
    path('chart_list/', ChartAPIView.as_view(), name='chart_list'),
]
