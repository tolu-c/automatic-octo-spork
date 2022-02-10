from django.contrib import admin
from .models import Gender, Eoi, Education, Skill, Knowledge

# Register your models here.

admin.site.register(Gender)
admin.site.register(Eoi)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Knowledge)
