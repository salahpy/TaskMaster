from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks',null=True)

    def __str__(self):
        return self.title