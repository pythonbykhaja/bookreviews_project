from django.db import models


class Publisher(models.Model):
    """
    Publisher Model
    """
    name = models.CharField(max_length=100, help_text='The name of the publisher')
    website = models.URLField(blank='', help_text='The Publishers website')
    email = models.EmailField(blank='', help_text='The Publishers email')


class Book(models.Model):
    """
    Book Model
    """
    title = models.CharField(max_length=100, help_text="The title of the book")
    publication_date = models.DateField(verbose_name='Date when the book was published')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
