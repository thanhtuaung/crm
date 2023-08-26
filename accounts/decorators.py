from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_fun(request, *args, **kwargs)
    return wrapper_fun

def allowed_users(allowed_roles=[]):
    def decorator(view_fun):
        def wrapper_fun(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.first().name
            
            if group in allowed_roles:
                return view_fun(request, *args, **kwargs)
            else:
                return HttpResponse("User can't access this page")
        return wrapper_fun
    return decorator



def admin_only(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.first().name

        if group == 'customer':
            return redirect('user-page')
        
        if group == 'admin':
            return view_fun(request, *args, **kwargs)
    return wrapper_fun