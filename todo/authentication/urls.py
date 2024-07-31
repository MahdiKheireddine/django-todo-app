from django.urls import path
from .views import RegistrationView, LoginView, LogoutView,check_auth_status

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('check-auth-status/', check_auth_status, name='check_auth_status'),
]
