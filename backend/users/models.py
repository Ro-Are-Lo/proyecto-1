from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, role='usuario'):
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")
        email = self.normalize_email(email) if email else None
        user = self.model(username=username, email=email, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(username=username, email=email, password=password, role='superadmin')
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    ROLES = (
        ('usuario', 'Usuario'),
        ('admin', 'Administrador'),
        ('superadmin', 'Super Administrador'),
    )
    email = models.EmailField(unique=True, null=True, blank=True)  # Agregar email
    role = models.CharField(max_length=20, choices=ROLES, default='usuario')

    objects = CustomUserManager()