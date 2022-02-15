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


'''
email => emailfield
fullname => charfield
gender:. => foreign key
phone number => charfield
state of residence => charfield
level of education: => foreign key
technical skills => foreign key
basic knowledge: boolean => foreign key
description of most challenging => charfield
worked on any projects => charfield
breif about your tech career journey => charfield
github url => url field
why wanna join the network with => charfield
tandc => foreign key
'''
