from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Resume(models.Model):
    position_title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    e_mail = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    education = models.CharField(max_length=500)
    languages_skills = models.CharField(max_length=200)
    skills = models.TextField()
    additional_information = models.TextField()

    def __str__(self):
        return self.position_title
