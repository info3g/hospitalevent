from django.http import HttpResponseRedirect

def user_is_valid(function):
    def wrap(request, *args, **kwargs):
        session = request.session  # this is a dictionary with session keys
        user = request.user

        if 'userid' in request.session.keys():
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/crud/signin/')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


