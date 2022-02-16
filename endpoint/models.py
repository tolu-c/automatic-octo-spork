from django.db import models

# Create your models here.


class Gender(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Knowledge(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Eoi(models.Model):
    fullname = models.CharField(max_length=255, default='Enter your full name')
    email = models.EmailField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=False)
    phone = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    education = models.ForeignKey(
        Education, on_delete=models.CASCADE, null=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=False)
    knowledge = models.ForeignKey(
        Knowledge, on_delete=models.CASCADE, null=False)
    chanllenges = models.CharField(max_length=255, blank=True)
    projects_details = models.CharField(max_length=255, blank=True)
    career_brief = models.CharField(max_length=255, blank=True)
    github_url = models.URLField(blank=True, null=True)
    join_network = models.CharField(max_length=255, blank=True)
    tnc = models.BooleanField(default=True)

    def __str__(self):
        return self.email
