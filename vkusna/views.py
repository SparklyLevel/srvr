from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from vkusna.models import User

# Create your views here.
def hi(request):
    return render(request, 'index.html')

def byebye(request):
    return HttpResponse('hewwo')

def UsersList(request):
    users = User.objects.all().values('id', 'name', 'age', 'birth_date', 'IsFemboy')
    users_list = list(users) 
    return JsonResponse(users_list, safe=False)