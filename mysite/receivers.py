from django.dispatch import receiver
from .models import promisAnswers, treatments, symptoms, diseases, userProfile, userProfileSymptom, userProfileSymptomUpdate, userProfileTreatment

from allauth.account.signals import password_changed
from allauth.account.signals import  user_signed_up
from allauth.account.signals import  user_logged_in

from pinax.eventlog.models import log


@receiver(user_logged_in)
def handle_user_logged_in(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_LOGGED_IN",
        extra={}
    )


@receiver(password_changed)
def handle_password_changed(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="PASSWORD_CHANGED",
        extra={}
    )






@receiver(user_signed_up)
def handle_user_signed_up(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_SIGNED_UP",
        extra={}
    )
