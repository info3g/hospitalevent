from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import datetime


class promisAnswers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    date = models.DateField(null=True)
    title = models.CharField(max_length=50)
    answers = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return self.title + ' - ' + (self.user) + ' - ' + (self.date) + ' - Score:'+ (self.score)

class treatments(models.Model):

    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Treatments"
    def __str__ (self):
        return self.name

class symptoms(models.Model):
    name = models.CharField(max_length=150)
    treatments = models.ManyToManyField(treatments,blank=True)
    type = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Symptoms"
    def __str__ (self):
        return self.name

class diseases(models.Model):
    name = models.CharField(max_length=150)
    symptoms = models.ManyToManyField(symptoms,blank=True)
    treatments = models.ManyToManyField(treatments,blank=True)

    class Meta:
        verbose_name_plural = "Diseases"
    def __str__(self):
        return self.name

class userProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    disease = models.ForeignKey(diseases, on_delete=models.CASCADE,default=1)
    usersymptoms = models.ManyToManyField(symptoms,through='userProfileSymptom')
    usertreatments = models.ManyToManyField(treatments, through='userProfileTreatment')
    about = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="images/userprofilepics",default='blog/images/news-newsletter-newspaper-information-158651_5PJlC13.png', editable=False)
    __original_name = None

    def __init__(self, *args, **kwargs):
        super(userProfile, self).__init__(*args, **kwargs)
        self.__original_name = self.image

    def save(self):
        if self.image != self.__original_name:

            im = Image.open(self.image)

            output = BytesIO()

            # Resize/modify the image
            width, height = im.size


            im = ImageOps.fit(im, [50,50], Image.ANTIALIAS)

            # after modifications, save it to the output
            im.save(output, format='png', quality=100)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.image.name.split('.')[0], 'image/jpeg',
                                              sys.getsizeof(output), None)

        super(userProfile, self).save()
        self.__original_name = self.image

    def __str__(self):
        return (self.user)

class userProfileSymptom(models.Model):
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, default=1)
    symptom = models.ForeignKey(symptoms, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return (self.user) +" "+ (self.symptom)

class userProfileSymptomUpdate(models.Model):
    symptom = models.ForeignKey(userProfileSymptom, on_delete=models.CASCADE, default=1)
    date = models.DateField(null=True)
    level = models.IntegerField()
    def __str__(self):
        return (self.symptom) +" "+ (self.date) +" "+ (self.level)

class userProfileTreatment(models.Model):
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, default=1)
    treatment = models.ForeignKey(treatments, on_delete=models.CASCADE, default=1)
    datestarted = models.DateField(null=True)
    dateended = models.DateField(null=True)
    dosage = models.CharField(max_length=10)
    overallsatisfaction = models.IntegerField()
    def __str__(self):
        return (self.user) +" "+ (self.treatment) + " "+(self.dosage) +" " + (self.datestarted) +" "+ (self.dateended)

class message(models.Model):
    recieved = models.ForeignKey(userProfile, on_delete=models.CASCADE, default=1,  related_name="userrecieved")
    sent = models.ForeignKey(userProfile, on_delete=models.CASCADE, default=1,  related_name="usersent")
    title = models.CharField(max_length=50)
    body = models.TextField()
    datesent = models.DateField(null=True)
    read = models.BooleanField(default=0)

    def __str__(self):
        return (self.title) + " to: " + (self.recieved) + " from: "+(self.sent)

class notification(models.Model):
    typechoices = (
        ('msg', 'Message'),
        ('event', 'Event'),
        ('other', 'Other'),

    )
    type = models.CharField(
        max_length=5,
        choices=typechoices,
        default="Message",
    )
    recieved = models.ForeignKey(userProfile, on_delete=models.CASCADE, default=1, related_name="reciever")
    datesent = models.DateField(null=True)
    message = models.ForeignKey(message, on_delete=models.CASCADE, null=True, blank=True)
    sentby = models.ForeignKey(userProfile, on_delete=models.CASCADE, default=1,  related_name="sentby")

    title = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

class event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(null=True)

    body = models.TextField()
    image = models.ImageField(upload_to="images/eventpics",
                              default='blog/images/news-newsletter-newspaper-information-158651_5PJlC13.png',editable=False)
    location = models.CharField(max_length=200)
    __original_name = None

    def __init__(self, *args, **kwargs):
        super(userProfile, self).__init__(*args, **kwargs)
        self.__original_name = self.image

    def save(self):
        if self.image != self.__original_name:
            im = Image.open(self.image)

            output = BytesIO()

            # Resize/modify the image
            width, height = im.size

            im = ImageOps.fit(im, [50, 50], Image.ANTIALIAS)

            # after modifications, save it to the output
            im.save(output, format='png', quality=100)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.image.name.split('.')[0],
                                              'image/jpeg',
                                              sys.getsizeof(output), None)

        super(userProfile, self).save()
        self.__original_name = self.image

    def __str__(self):
        return (self.title) + " " + (self.date)

class promisquestions(models.Model):

    orderChoices = (
        ('low', 'low'),
        ('high', 'high'),

    )

    title = models.CharField(max_length=100)
    questions = models.TextField()
    nanswers = models.IntegerField()
    order = models.CharField(
        max_length=5,
        choices=orderChoices,
        default="High",
    )
