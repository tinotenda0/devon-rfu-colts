from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def admin_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not (request.user.is_superuser or (hasattr(request.user, 'role') and request.user.role == 'admin')):
            if request.user.role == 'club_admin':
                return redirect('club_admin_dash')
            else:
                return HttpResponseForbidden("Admin access required.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def club_admin_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.role == 'club_admin':
            return HttpResponseForbidden("Club Admin access required.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
