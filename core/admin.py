from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from core.models import User, UserConfiguration

admin.site.register(User, UserAdmin)
admin.site.register(UserConfiguration)
