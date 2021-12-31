from django.contrib import admin
from .models import Fragment, User, Profile
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Fragment)