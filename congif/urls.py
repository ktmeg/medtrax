"""congif URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views
from core.views import UserSignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('registration.backends.default.urls')),
    # path('', include('django_registration.backends.activation.urls')),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view, name='password_change_done'),
    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # path('accounts/login/', include('django.contrib.auth.views.login'),
    #      {'template_name': 'registration/login.html'}),
    path('accounts/signup/', UserSignUpView.as_view(), name='signup'),
    path('', views.dashboard, name='dashboard'),
    path('med/<int:pk>', views.med, name='med'),
    path('new-med/', views.new_med, name="new_med"),
    path('edit-med/<int:pk>', views.edit_med, name="edit_med"),
    path('delete-med/<int:pk>/', views.delete_med, name='delete_med'),


]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


# path('accounts/password_change/done/',
#      auth_views.PasswordChangeDoneView.as_view, name='password_change_done'),
# path('accounts/password_reset/',
#      auth_views.PasswordResetView.as_view(), name='password_reset'),
# path('accounts/password_reset/done/',
#      auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
# path('accounts/reset/<uidb64>/<token>/',
#      auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
# path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(),
#      name='password_reset_complete'),
# path('accounts/', include('registration.backends.simple.urls')),
# path('login', views.login_view, name='login'),

# path('accounts/login/',
#      auth_views.LoginView.as_view(template_name='registration/login.html')),
