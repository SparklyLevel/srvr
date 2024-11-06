from django.shortcuts import render
from django.http import HttpResponse

from vkusna.models import User
# Create your views here.
def hi(request):
    return HttpResponse('hewwo')

def byebye(request):
    return render(request, 'index.html')

def UsersList(request):
    users= User.objects.all()
    return render(request, 'Userslist.html', context={'users':users})