from django.contrib import admin
from CrowdJournal.models import News,UserProfile,Argument
# Register your models here.
admin.site.register(News)
admin.site.register(Argument)
admin.site.register(UserProfile)