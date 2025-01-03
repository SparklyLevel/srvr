from django.contrib import admin

from vkusna.models import User, Image, Ff, Video

@admin.register(User)
class UserAdmin(admin.ModelAdmin): 
    list_display = ['id', 'name', 'age', 'birth_date', 'IsFemboy']
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin): 
    list_display = ['id', 'title', 'user', 'path']
    
@admin.register(Ff)
class FfAdmin(admin.ModelAdmin): 
    list_display = ['id', 'title', 'Number_of_views', 'Dumbness']
    
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin): 
    list_display = ['id', 'length', 'description', 'path']