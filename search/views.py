from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from home.models import Event_Management
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password

from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout
from wagtail.core.models import Page
from wagtail.search.models import Query


from django.shortcuts import render

from crud.models import Signup

# Create your views here.


def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
def dashboard(request):
    event_list = Event_Management.objects.all().order_by('id')
    user_id=request.user.id
    print(user_id)
    print ("hyyyyyyyyyy")
    context={ 'event_list': event_list }
    return render(request, 'search/dashboard.html', context)


def link(request):

    event_id=request.GET.get('id')
    print("eventid")
    print(event_id)
    event_list = Event_Management.objects.filter(id=event_id)
    print(event_list)
    print("eventlist")
    context={'event_list' : event_list}
    return render(request, 'search/link.html', context)





def contact(request):
    context={}
    return render(request, 'search/contact.html', context)

# def logoout(request):
#     context={}
#     return render(request, 'search/logout.html', context)

def user_profile(request):
    user_id=request.user.id
    user_profile=Signup.objects.get(id=user_id)
    print(user_profile)
    print(user_profile.date_of_birth)
    context={'user_profile': user_profile}
    return render(request, 'search/userinfo.html', context)

# def edit(request):
#     user_id=request.user.id
#     print(user_id)
#     userupdate=Signup.objects.get(id=user_id)
#     print(userupdate)
#     context={'user_profile':userupdate}
#     return render(request, 'search/edit.html', context)


# def update(request):
#      if request.method=='POST':
#          houseid = request.POST["hdnId"]
#          print(houseid)
#          #username=request.POST["username"]
#          email=request.POST["email"]
#          conditions=request.POST["conditions"]
#          category=request.POST["category"]
#
#          rsObj = Signup.objects.get(id=houseid)
#          print(rsObj)
#          #dsovj.username=username
#          rsObj.email=email
#          rsObj.conditions=conditions
#          rsObj.category=category
#          rsObj.save()
#
#          messages.add_message(request, messages.INFO, 'congrats your profile is updated.')

     # context={}
     # return render(request, 'search/userinfo.html', context)


def edit_info(request):
    user_id=request.user.id
    #houseid = request.POST["hdnId"]
#          print(houseid)

    print(user_id)
    userupdate=Signup.objects.get(id=user_id)
    print(userupdate)
    print(userupdate.date_of_birth)
    context={'user_profile':userupdate}
    return render(request, 'search/edit_basic.html', context)

def update_basic_info(request):
    if request.method=="POST":
        hdn=request.user.id
        print(hdn)
        firstname = request.POST["fname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        conditions = request.POST["conditions"]
        category = request.POST["category"]
        adate = request.POST["date"]
        print(adate)
        gender=request.POST["gender"]


        print("gffffffffffffffj")
        dsovj = Signup.objects.get(id=hdn)
        dsovj.firstname = firstname
        dsovj.lastname = lastname
        dsovj.date_of_birth = adate
        dsovj.gender=gender
        dsovj.email=email
        dsovj.conditions=conditions
        dsovj.category=category

        dsovj.save()
        messages.add_message(request, messages.INFO,  'your profile is updated.')
        return HttpResponseRedirect("/search/user_profile/")
    context = {}
    return render(request, 'search/userinfo.html', context)






def update_password(request):
    context={}
    if request.method=="POST":
        user_id = request.POST["hdnId"]
        old_password=request.POST["old_password"]
        new_password=request.POST["password"]
        conf_new_password=request.POST["confirmpassword"]
        user_id=request.user.id
        print(user_id)
        user=request.user
        print(user)
        raw_password=request.user.password
        print(raw_password)

        x=user.check_password('{}'.format(old_password))
        print(x)

        if x:
            print("ififififi")
            rsObj = Signup.objects.get(id=user_id)
            print(rsObj)
            rsObj.set_password(new_password)
            print("********")
            rsObj.save()
            print("hyyyyyyyyydgdgdgdhdgdgdgd")
            messages.add_message(request, messages.INFO, 'You have Successfully update your password, So you have to Login First')
            return HttpResponseRedirect("/crud/signin/")
        else:
            messages.error(request, 'Sorry, Please enter your correct old password')
    return render(request, 'search/update_password.html', context)

def basic(request):
    context={}
    return render(request, 'search/terms.html', context)

def edit_photo(request):
    user_id = request.user.id


    print(user_id)
    userupdate = Signup.objects.get(id=user_id)
    print(userupdate)
    context = {'user_profile': userupdate}
    return render(request, 'search/photoedit.html', context)


def update_photo(request):
    if request.method=="POST":
        hdn = request.user.id
        print(hdn)
        aimage = request.FILES["aimage"]
        fs = FileSystemStorage()
        filename = fs.save(aimage.name, aimage)
        dsovj = Signup.objects.get(id=hdn)
        dsovj.aimage = aimage
        dsovj.save()
        messages.add_message(request, messages.INFO, 'your profile is updated.')
        return HttpResponseRedirect("/search/user_profile/")


    context = {}
    return render(request, 'search/userinfo.html', context)


