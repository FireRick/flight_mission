from django.urls import path

from accounts.views import (
    profile_view, ClientLoginView, ClientLogoutView,
    ClientPasswordChangeView, ClientPasswordChangeDoneView,
    ClientPasswordResetView, ClientPasswordResetDoneView,
    ClientPasswordResetConfirmView, ClientPasswordResetCompleteView,
)

# app_name = 'accounts'
urlpatterns = [
    path('login/', ClientLoginView.as_view(), name='login'),
    path('logout/', ClientLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('password_change/', ClientPasswordChangeView.as_view(),
        name='password_change'),
    path('password_change/done/', ClientPasswordChangeDoneView.as_view(),
        name='password_change_done'),
    path('password_reset/', ClientPasswordResetView.as_view(),
        name='password_reset'),
    path('password_reset/done/', ClientPasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ClientPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset/done/', ClientPasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]
