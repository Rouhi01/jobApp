from django.db import models


NEWSLETTER_OPTION = [
    ('W', 'Weekly'),
    ('M', 'Monthly'),
]


class Subscribe(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    option = models.CharField(max_length=2, choices=NEWSLETTER_OPTION)
