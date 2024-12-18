from django.urls import path
from apps.custom_user.api.views import (
    UserRegistrationView, LoginUserView, LogoutView,
    ChangePasswordView, ResetPasswordView, UserCountView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', LoginUserView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('user-count/', UserCountView.as_view(), name='user_count'),
]
