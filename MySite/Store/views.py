from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Store.models import MoveItem
from django.db.models import Sum
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


# авторизация
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "Store/auth.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


# подсчет количество материалов на складе и подсчет расхода материалов

@login_required
def home(request):
    sumas = MoveItem.objects.filter(date_out__isnull=False).values('name__name', 'type__name','date_out',
                                                                   'tip').annotate(summaout=Sum('count'))
    cons = MoveItem.objects.values('name__name', 'type__name','type__firm__name').annotate(summa=Sum('count'))
    return render(request, 'Store/home.html', {'sumas': sumas, 'cons': cons})
