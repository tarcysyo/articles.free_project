from django.contrib.auth import views as auth_views
from django.urls import re_path


urlpatterns = [
    re_path(r'^entrar/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login',),
    re_path(r'^sair/$', auth_views.LogoutView.as_view(next_page='core:home'), name='logout',),
]