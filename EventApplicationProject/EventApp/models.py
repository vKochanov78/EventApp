from django.db import models
from django.core.validators import MinLengthValidator

from .validators import validate_name,\
                        validate_password,\
                        validate_future_date


class ProfileModel(models.Model):

    first_name = models.CharField(max_length=20, validators=[validate_name])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(4)])
    email = models.EmailField(max_length=45)
    profile_picture = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(5), validate_password])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EventModel(models.Model):
    EVENT_CATEGORIES = [
        ('Sports', 'Sports'),
        ('Festivals', 'Festivals'),
        ('Conferences', 'Conferences'),
        ('Performing Art', 'Performing Art'),
        ('Concerts', 'Concerts'),
        ('Theme Party', 'Theme Party'),
        ('Other', 'Other'),
    ]

    event_name = models.CharField(max_length=30, validators=[MinLengthValidator(2)])
    category = models.CharField(max_length=20, choices=EVENT_CATEGORIES)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(validators=[validate_future_date])
    event_image = models.URLField()

    def __str__(self):
        return self.event_name

