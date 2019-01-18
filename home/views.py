from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from home.models import Event_Management
from django.contrib.auth.decorators import login_required
from .decorator import user_is_valid


@login_required(login_url = '/crud/signin/')
#@user_is_valid
def index(request):
    event_list = Event_Management.objects.all().order_by('id')
    context={ 'event_list': event_list }
    return render(request, 'home/index.html', context)

def event(request):
    event_list = Event_Management.objects.all().order_by('id')
    context={ 'event_list': event_list }
    return render(request, 'home/index.html', context)

def thanks(request):
    context={}
    return render(request, 'home/thanks.html', context)


# def dismissed(request):
#     mess = request.POST.get("value")
#     dsovj = eventdismis()
#     dsovj.message = mess
#     dsovj.save()
#
#     context = {}
#     return render(request, 'home/dismiss.html', context)
#




