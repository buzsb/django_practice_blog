from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Resume(models.Model):
    position_title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    e_mail = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    education = models.CharField(max_length=500)
    skills = models.TextField()
    additional_information = models.TextField()

    def __str__(self):
        return self.position_title


class Languages(models.Model):
    language = models.CharField(max_length=200)
    languages_levels = models.ManyToManyField(Resume, through='LanguageLevel')

    def __str__(self):
        return self.language


class LanguageLevel(models.Model):
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    language_level = models.CharField(max_length=200)
