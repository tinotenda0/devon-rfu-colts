from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def role_required(allowed_roles):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if (
                not hasattr(request.user, "role")
                or request.user.role not in allowed_roles
            ):
                return HttpResponseForbidden(
                    "Sorry you do not have permission to access this page."
                )
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator

def admin_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not (request.user.is_superuser or (hasattr(request.user, 'role') and request.user.role == 'admin')):
            return HttpResponseForbidden("Admin access required.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def club_admin_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser or not request.user.role == 'club_admin':
            return HttpResponseForbidden("Club Admin access required.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
