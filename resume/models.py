from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Resume(models.Model):
    vacancy_title = models.CharField(max_length=200)
