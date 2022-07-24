from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import *
from .forms import *

class ParametersGet(ListView):

    def get_years(self):
        years_sorted_list = sorted(set(Auto.objects.filter(is_published=True).values_list('year', flat=True)))
        return years_sorted_list
    def get_condition(self):
        condition_sorted_list = sorted(set(Auto.objects.filter(is_published=True).values_list('condition', flat=True)))
        return condition_sorted_list
    def get_firm(self):
        firm_sorted_list = sorted(set(Auto.objects.filter(is_published=True).values_list('firm', flat=True)))
        return firm_sorted_list
    def get_power(self):
        power_sorted_list = sorted(set(Auto.objects.filter(is_published=True).values_list('power', flat=True)))
        return power_sorted_list
    def get_mark(self):
        mark_sorted_list = sorted(set(Auto.objects.filter(is_published=True).values_list('mark', flat=True)))
        return mark_sorted_list

class AutoHome(ParametersGet,ListView):
    paginate_by = 9
    model = Auto
    template_name = 'shop/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = ParametersGet
        context['condition'] = ParametersGet
        return context

class AddPage(LoginRequiredMixin,CreateView):
    form_class = AddPostForm
    template_name = 'shop/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

class RegisterUser(CreateView):
    form_class =  RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user =form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'shop/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

class ShowPost(DetailView):
    model = Auto
    template_name = 'shop/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

class FilterAutoView(ParametersGet, ListView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        kwargs = {}
        if self.request.GET.getlist("year"):
            kwargs["year__in"] = self.request.GET.getlist("year")

        if self.request.GET.getlist("condition"):
            kwargs["condition__in"] = self.request.GET.getlist("condition")
            print(kwargs)

        if self.request.GET.getlist("engeer"):
            kwargs["fuel__in"] = self.request.GET.getlist("engeer")

        if self.request.GET.getlist("transmission"):
            print(self.request.GET.getlist("transmission"))
            kwargs["transmission__in"] = self.request.GET.getlist("transmission")

        if self.request.GET.getlist("firms"):
            strcheckfirm ="".join(self.request.GET.getlist("firms"))
            print("Firm ", strcheckfirm)
            if(strcheckfirm != '0'):
                kwargs["firm__in"] = self.request.GET.getlist("firms")
                print(kwargs["firm__in"])

        if self.request.GET.getlist("marks"):
            strcheckfirm ="".join(self.request.GET.getlist("marks"))
            print("Mark ", strcheckfirm)
            if(strcheckfirm != '0'):
                kwargs["mark__in"] = self.request.GET.getlist("marks")
                print(kwargs["mark__in"])

        if self.request.GET.getlist("powers"):
            strcheckfirm ="".join(self.request.GET.getlist("powers"))
            print(strcheckfirm)
            if(strcheckfirm != '0'):
                kwargs["power__in"] = self.request.GET.getlist("powers")

        if self.request.GET.getlist("distancefrom"):
            df = self.request.GET["distancefrom"]
            if len(df) != 0:
                kwargs["distance__gte"] = df

        if self.request.GET.getlist("distanceto"):
            dt = self.request.GET["distanceto"]
            if len(dt) != 0:
                kwargs["distance__lte"] = dt

        if self.request.GET.getlist("pricefrom"):
            pf = self.request.GET["pricefrom"]
            if len(pf) != 0:
                kwargs["price__gte"] = pf

        if self.request.GET.getlist("priceto"):
            pt = self.request.GET["priceto"]
            if len(pt) != 0:
                kwargs["price__lte"] = pt

        if self.request.GET.getlist("powerfrom"):
            powerf = self.request.GET["powerfrom"]
            if len(powerf) != 0:
                kwargs["price__gte"] = powerf

        if self.request.GET.getlist("powerto"):
            powert = self.request.GET["powerto"]
            if len(powert) != 0:
                kwargs["power__lte"] = powert


        queryset= Auto.objects.filter(**kwargs)
        print(queryset)
        return queryset

    model = get_queryset
    context_object_name = 'posts'
