from django.contrib import admin
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todolist.urls', namespace='todo')),
    path('', include('bboard.urls', namespace='bboard')),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='bboard:index'),
         name='logout'),

    path('accounts/password_change/', PasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('accounts/password_reset/', PasswordResetView.as_view(),
         name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
