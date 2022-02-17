from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Knowledge(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Eoi(models.Model):
    class Gender(models.TextChoices):
        Male = 'M', _('Male')
        Female = 'F', _('Female')
        Other = 'Other', _('Other')

    class Education(models.TextChoices):
        SSCE = 'SSCE', _('SSCE')
        OND = 'F', _('OND')
        HND = 'HND', _('HND')
        BSc = 'BSc', _('BSc')
        Undergraduate = 'Undergraduate', _('Undergraduate')

    fullname = models.CharField(max_length=255, default='Enter your full name')
    email = models.EmailField()
    gender = models.CharField(choices=Gender.choices,
                              null=False, max_length=10)
    phone = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    education = models.CharField(
        choices=Education.choices, null=False, max_length=255,)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=False)
    knowledge = models.ForeignKey(
        Knowledge, on_delete=models.CASCADE, null=False)
    challenges = models.CharField(max_length=255, blank=True)
    projects_details = models.CharField(max_length=255, blank=True)
    career_brief = models.CharField(max_length=255, blank=True)
    github_url = models.URLField(blank=True, null=True)
    join_network = models.CharField(max_length=255, blank=True)
    tnc = models.BooleanField(default=True)

    def __str__(self):
        return self.email
