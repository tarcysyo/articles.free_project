from django.contrib.auth import views as auth_views
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^entrar/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login', ),
    re_path(r'^sair/$', auth_views.LogoutView.as_view(next_page='core:home'), name='logout', ),
    re_path(r'^cadastrar/$', views.register, name='register', ),
    re_path(r'^painel/$', views.dashboard, name='dashboard', ),
    re_path(r'^publicar/$', views.publication, name='publication', ),
]