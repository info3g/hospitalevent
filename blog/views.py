from django.shortcuts import render
from django.shortcuts import render,redirect
import datetime
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import blogpost
from .forms import MyForm
# Create your views here.
def editpost(request, pk):
    print()
    instance = blogpost.objects.get(id=pk)
    print(instance)
    form = MyForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('home')

    return render(request, 'blogedit.html', {'form': form})
