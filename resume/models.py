from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Language(models.Model):
    language = models.CharField(max_length=200)

    def __str__(self):
        return self.language


class Person(models.Model):
    position_title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    e_mail = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    skype = models.CharField(max_length=30, blank=True, null=True)
    education = models.CharField(max_length=500)
    languages = models.ManyToManyField(Language, through='LanguageLevel')
    skills = models.TextField()
    additional_information = models.TextField()

    def __str__(self):
        return self.position_title


class LanguageLevel(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    resume = models.ForeignKey(Person, on_delete=models.CASCADE)
    level = models.CharField(max_length=200)
