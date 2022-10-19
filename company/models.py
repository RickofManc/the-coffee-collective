from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """
    Models the fields for the Contact Form.
    """
    name = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)
    date_submitted = models.DateTimeField(default=timezone.now)

    class Meta:
        """ Set verbose name """
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'
        ordering = ['-date_submitted']
