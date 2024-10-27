from django.contrib import admin

from vkusna.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin): 
    list_display = ['id', 'name', 'age', 'birth_date', 'IsFemboy']