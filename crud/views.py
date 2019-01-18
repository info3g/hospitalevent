from django.shortcuts import render,redirect
# Create your views here
from django.http import HttpResponseRedirect, JsonResponse
from .models import Signup
from home.models import Event_Management
from home.models import EventSelect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
import sys, json
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.core.files.storage import FileSystemStorage


from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import PermissionDenied

def signup(request):
    try:
        if request.method == "POST":
            print('welcome to register user.')
            username=request.POST["username"]
            password=request.POST["password"]
            confirmpassword=request.POST["confirmpassword"]
            email=request.POST["email"]
            conditions = request.POST["conditions"]
            category = request.POST["category"]
            dropdown = request.POST["dropdown"]
            x = Signup.objects.filter(email=email).count()
            print(x)
            if x > 0:
                messages.error(request, 'Sorry, This Email is already exist Please try again with another email')
            else:
                print('wwwwwwwwww')
                dsobj=Signup()
                dsobj.username=username
                    # print("password : ", dsobj.set_password(password))

                # dsobj.password = password
                dsobj.set_password(password)
                    # dsobj.password=password
                    #dsobj.password = make_password(password='testing',
                                        #  salt=None,
                                        #  )

                dsobj.email=email
                dsobj.conditions=conditions
                dsobj.position=dropdown
                dsobj.category=category
                dsobj.save()
                messages.add_message(request, messages.INFO, 'You have Successfully Register your account')

                print('kkkkkkkkkkkkkkkkk')

    except:
        print('eeeeeeeeeeeeeeeeeeeeeeee')
        print(sys.exc_info())
    context = {}
    return render(request, 'crud/signup.html', context)

def basic(request):
    context={}
    print('bbbbbbbbbbbbbbbbbbbb')
    print(request.user.last_login)
    if request.user.last_login is None:
        if request.method == 'POST':
            print("Going to post data:")
            hdnId = request.POST["hdnid"]
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            adate = request.POST["date"]
            image = request.FILES["image"]
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            gender = request.POST["gender"]
            print("gffffffffffffffj")
            dsovj = Signup.objects.get(id=hdnId)
            dsovj.firstname = firstname
            dsovj.lastname = lastname
            dsovj.date_of_birth = adate
            dsovj.gender = gender
            dsovj.aimage = image
            dsovj.save()
            return HttpResponseRedirect('/crud/basic_list/')
    else:
        user_id = request.user.id
        print(user_id)
        user_profile = Signup.objects.filter(id=user_id).all()
        print(user_profile)
        context = {'user_profile': user_profile}
        return render(request, 'search/userinfo.html', context)





def basic_list(request):
    user_id = request.user.id
    print(user_id)
    user_profile = Signup.objects.filter(id=user_id)
    print(user_profile)
    context = {'user_profile': user_profile}
    return render(request, 'search/basicinfo.html', context)


def forget(request):
    context={}
    if request.method=="POST":
        email=request.POST["email"]
        check=Signup.objects.filter(email=email)
        print(check)
        if check:
            send_email_forget_password(email)
            messages.add_message(request, messages.INFO, 'Email send sucessfully, please check your email')

        else:
            messages.add_message(request, messages.INFO, 'Sorry, This Email is Not valid.')




    return render(request, 'search/forget.html', context)

def send_email_forget_password(email):
    context={}
    subject = "forget password"
    message = "click on  <a href='//127.0.0.1:8000/crud/reset-password/?q="+ email +"'>this link</a> for reset your password"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list)


    print("email sends succesfully")

def reset_password(request):

    email = request.GET.get("q")
    print("wwwwwwwwww : ")
    print(email)
    if request.method=="POST":
        print("ghvvvvvvvvv")
        password=request.POST["password"]
        confirmpassword=request.POST["confirmpassword"]
        email=request.POST["email"]
        dsovj=Signup.objects.get(email=email)
        dsovj.password=password
        #dsovj.password=make_password(password)
        print(dsovj)
        dsovj.save()
        messages.add_message(request, messages.INFO, 'Your password is sucessfully updated ')




    context = {
        'email':email
    }
    return render(request, 'search/reset-password.html', context)




def I_am_going(request):
    context={
        'error': False
    }
    print("Going to submit event.")
    user_id = request.user.id
    #user_id = 26

    print(user_id)
    mess=request.POST.get("value")
    print(mess)
    event_id=request.POST.get('event_id')
    print("dhdhhdhd")

    print(event_id)
    check=EventSelect.objects.filter(user_id=user_id, event_id=event_id, message=mess).count()
    print(check)
    if check>0:
        if mess=="Yes":
            mess = "Sorry, You are already subscribed for this event!"
        else:
            mess="Thanks for register with event"
        context.update({'error': True})
        context.update({"message": mess})
            #message="hghgujguguguuugggug"
        # mess=messages.error(request, 'The submission deadline has passed!', extra_tags='alert')
        print(mess)
        print('qqqqqqqqqqqqq')
        print(json.dumps(context))
        return JsonResponse(context)

        # raise PermissionDenied



    else:
        objEM = Event_Management.objects.get(id=event_id)
        objES = EventSelect()
        print(objES)
        objES.user_id = user_id
        objES.event = objEM
        objES.message = mess
        objES.save()

        context.update({'error': True})
        context.update({"message": "Thanks for Register we will update you very soon"})
        #messages.success(request, 'Thanks for Register we will update you very soon')


    print("this is correct")
    return JsonResponse(context)






def event_list_admin(request, event_management_id=None):
    context = {}
    event_management_id = request.GET.get('q')
    if event_management_id:
        event_select_list = EventSelect.objects.filter(event_id=event_management_id)

        user_ids = [int(u.user_id) for u in event_select_list]
        user_ids = set(user_ids)
        event_users = Signup.objects.filter(id__in=user_ids)
        user_data = []
        for user in event_users:
            d = {
                'username': user.username,
                'email': user.email,
                'conditions': user.conditions,
                'category': user.category,
                'position': user.position,
                'message1': '-empty-',
                'message2': '-empty-'
            }
            user_events_list = EventSelect.objects.filter(user_id=user.pk)
            for event in user_events_list:
                if event.message == "Yes":
                    d.update({'message1': event.message})
                else:
                    d.update({'message2': event.message})
            user_data.append(d)
            context.update({'event_users': user_data})

    return render(request, 'crud/event_users_list.html', context)


def signin(request):
    context={}
    if request.method=="POST":
        rusername=request.POST["username"]
        rpassword=request.POST["password"]
        print("rusername : ",rusername)
        print("rpassword : ",rpassword)
        # objUser=Signup.objects.filter(username=rusername, password=rpassword)
        objUser = authenticate(username=rusername, password=rpassword)
        print("bfhfhhvf")
        print(objUser)

        user_id = request.user.id
        #user_id = objUser.id
        print('user_id : ',user_id)
       # objUser=Signup.objects.auth(username=rusername, password=rpassword)
       # print(objUser)
        if objUser is not None and objUser.is_active:
            auth_views.login(request, objUser)
            messages.add_message(request, messages.INFO, "login succesfully")
            return redirect('/search/dashboard/')

        else:
            messages.add_message(request, messages.INFO, 'Sorry This Username or password is Not valid.')

    return render(request, 'search/signin.html', context)


def pagelogout(request):
    logout(request)
    context={}
    return render(request, 'search/logout.html', context)
