from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email,first_name, last_name,age,password):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            age = age,
            password = password
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, last_name, age,password):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            age = age,
            password = password
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','age']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label = None):
        return self.is_admin

    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email


