from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import promisAnswers, userProfile, userProfileSymptomUpdate, userProfileSymptom, symptoms
from django.template import loader

def MyView(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        date = datetime.date.today()
        score = 0
        answers = []
        title = request.POST.get("formname","")
        for key in request.POST:
            if 'q' in key:
                answers.append(request.POST[key])
                score = score + int(request.POST[key])
        print(user)
        formanswers = promisAnswers(user=user,date=date,title=title,answers=answers,score=score)
        profile = userProfile.objects.get(user=user)
        symptom = symptoms.objects.get(name=title)
        try:
            ups = userProfileSymptom.objects.get(user=profile,symptom=symptom)
        except:
            ups = userProfileSymptom(user=profile, symptom=symptom)
            ups.save()
        upsu = userProfileSymptomUpdate(symptom=ups, date=datetime.datetime.now(), level =score)
        upsu.save()

        formanswers.save()


        context = {}

    return render(request, "forms/promis/multipageform.html")

