from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from vkusna.models import User, Image, Ff, Video
from django.conf import settings

# Create your views here.
def hi(request):
    return render(request, 'index.html')

def byebye(request):
    return HttpResponse('hewwo')

def UsersList(request):
    users = User.objects.all().values('id', 'name', 'age', 'birth_date', 'IsFemboy')
    ff = Ff.objects.all().values('id', 'title','Number_of_views','Dumbness')
    video = Video.objects.all().values('id', 'length','description')
    users_list = list(users) 
    ff_list=list(ff)
    video_list=list(video)
    return JsonResponse(users_list, safe=False)

def V(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'Videos.html', context)