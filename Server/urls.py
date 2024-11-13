from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vkusna.views import byebye, hi, UsersList

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', hi, name = 'main'),    
    path('bye/', byebye, name = 'nemain'),    
    path('users/', UsersList, name = 'userList')
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
