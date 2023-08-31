from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    USER_TYPE = (
        ('Client', 'Client'),
        ('VipClient', 'VipClient'),
        ('BigBoss', 'BigBoss')
    )

    GENDER = (
        ('M', 'M'),
        ('Ж', 'Ж')
    )

    user_type = models.CharField(max_length=100, choices=USER_TYPE)
    phone_number = models.CharField(max_length=13, default="+996", null=True)
    age = models.PositiveIntegerField(default=18)
    gender = models.CharField(max_length=100, choices=GENDER)

