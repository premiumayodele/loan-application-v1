from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from . forms import UserLoginForm

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html')), #authentication_form=UserLoginForm)),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=UserLoginForm)),
    path('logout/', auth_views.LogoutView.as_view(), name="user_logout" ),
    path('register/', views.register, name="register" ),
    # path('account/password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    # path('account/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    # path('account/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('account/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', views.complete_profile, name='complete_profile'),
]