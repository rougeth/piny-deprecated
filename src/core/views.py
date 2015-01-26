from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class LoginRequeredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequeredMixin, self).dispatch(*args, **kwargs)

class HomeView(LoginRequeredMixin, TemplateView):
    template_name = 'core/home.html'
