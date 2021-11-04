from django.urls import path, include

from .views import HomeView, SignupView, LoginView, LogoutView, PermissionsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/', include('main.api.urls')),
    path('permissions/', PermissionsView.as_view(), name='permissions'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
