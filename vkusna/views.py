from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from vkusna.models import User, Ff, Video, 

# Create your views here.
def hi(request):
    return render(request, 'index.html')

def byebye(request):
    return HttpResponse('hewwo')

def UsersList(request):
    users = User.objects.all().values('id', 'name', 'age', 'birth_date', 'IsFemboy')
    users_list = list(users) 
    return JsonResponse(users_list, safe=False)

def FfList (request):
    ff = Ff.objects.all().values('id', 'title','Number_of_views','dumbness')
    ff_list = list(ff)
    return JsonResponse(ff_list,safe=False)

def VideoList(request):
    video = Video.objects.all().values('id', 'length','description')
    video_list=list(video)
    return JsonResponse(video_list,safe=False)

