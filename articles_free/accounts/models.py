# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin, UserManager
# from django.db import models
#
# # Create your models here.
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField('Username', max_length=30, unique=True)
#     email = models.EmailField('E-mail', unique=True)
#     name = models.CharField('Nome', max_length=50, blank=False, null=False)
#     surname = models.CharField('Sobrenome', max_length=150, blank=False, null=False)
#     is_active = models.BooleanField('Está ativo?', blank=False, default=True)
#     is_staff = models.BooleanField('É da equipe?', blank=False, default=False)
#     date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'name', 'surname']
#
#     def __str__(self):
#         return self.name+self.surname or self.username
#
#     def get_short_name(self):
#         return self.username
#
#     def get_full_name(self):
#         return str(self)
#
#     class Meta:
#         verbose_name = 'Usuário'
#         verbose_name_plural = 'Usuários'