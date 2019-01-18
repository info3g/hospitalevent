from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(promisAnswers)
admin.site.register(diseases)
admin.site.register(symptoms)
admin.site.register(treatments)
admin.site.register(userProfile)
admin.site.register(userProfileSymptom)
admin.site.register(userProfileSymptomUpdate)
admin.site.register(userProfileTreatment)
admin.site.register(message)
admin.site.register(event)
admin.site.register(promisquestions)