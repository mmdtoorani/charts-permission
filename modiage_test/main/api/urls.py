from django.urls import path

from .views import StaffListAPIView, ChartAPIView, ChangePermissionsAPIView

urlpatterns = [
    path('staff_list/', StaffListAPIView.as_view(), name='staff_list'),
    path('chart_list/', ChartAPIView.as_view(), name='chart_list'),
    path('change_permissions/', ChangePermissionsAPIView.as_view(), name='change_permissions'),
]
