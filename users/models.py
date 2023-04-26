import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import redirect
from oauth2_provider.models import Application as OAuth2Application
from .email_sender import *


class Application(OAuth2Application):
    class Meta(OAuth2Application.Meta):
        app_label = 'Habit tracker'


class User(AbstractUser):

    def auth_user(cls, data):

        emailCode = random.randint(10000, 99999)
        send_email('Код', emailCode, data['email'])
        # Approving_mail(username=data['code'], email=data['email'], url=redirect('register'))

    @classmethod
    def create_from_post(cls, data):

        instance = cls(password=data['password'], email=data['email'])
        instance.save()

        return instance

