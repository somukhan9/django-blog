from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# required imports to validate unique email constraints before saving super user or user
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    profile_picture = models.ImageField(
        upload_to='uploads/users', null=True, blank=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]


@receiver(pre_save, sender=User)
def check_email(sender, instance, **kwargs):
    email = instance.email

    if User.objects.filter(email=email).exclude(username=instance.username).exists():
        raise ValidationError(
            {"field": "email", "message": "A user with that email already exists."})


@receiver(pre_save, sender=User)
def check_username(sender, instance, **kwargs):
    username = instance.username
    if User.objects.filter(username=username).exclude(email=instance.email).exists():
        raise ValidationError(
            {"field": "username", "message": "A user with that username already exists."})
