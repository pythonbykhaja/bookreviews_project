from django.db import models


class Publisher(models.Model):
    """
    Publisher Model
    """
    name = models.CharField(max_length=100, help_text='The name of the publisher')
    website = models.URLField(blank='', help_text='The Publishers website')
    email = models.EmailField(blank='', help_text='The Publishers email')
