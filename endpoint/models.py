from django.db import models


class Eoi(models.Model):
    fullname = models.CharField(max_length=255, default='Enter your full name')
    email = models.EmailField()
    gender = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    education = models.CharField(max_length=255, blank=False)
    skill = models.CharField(max_length=255, blank=False)
    knowledge = models.CharField(max_length=255, blank=False)
    challenges = models.CharField(max_length=255, blank=True)
    projects_details = models.CharField(max_length=255, blank=True)
    career_brief = models.CharField(max_length=255, blank=True)
    github_url = models.URLField(blank=True, null=True)
    join_network = models.CharField(max_length=255, blank=True)
    tnc = models.BooleanField(default=True)

    def __str__(self):
        return self.email
