from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from market.forms import UserForm, AdministratorForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from market.models import Administrator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class AdminRegisterView(View):
    def get(self, request):
        return render(request, 'admin_register.html')

    def post(self, request):
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            admin_form = AdministratorForm(data=request.POST)
            if user_form.is_valid() and admin_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                admin = admin_form.save(commit=False)
                admin.user = user
                if 'avatar' in request.FILES:
                    admin.avatar = request.FILES['avatar']
                admin.save()
                registered = True
            else:
                print(user_form.errors, admin_form.errors)
        else:
            user_form = UserForm
            admin_form = AdministratorForm()
        return render(request, 'admin_register.html', {'user_form': user_form,
                                                       'admin_form': admin_form,
                                                       'registered': registered})


class CustomerRegisterView(View):
    def get(self, request):
        return render(request, 'customer_register.html')

    def post(self, request):
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            customer_form = CustomerForm(data=request.POST)
            if user_form.is_valid() and customer_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                customer = customer_form.save(commit=False)
                customer.user = user
                if 'avatar' in request.FILES:
                    customer.avatar = request.FILES['avatar']
                customer.save()
                registered = True
            else:
                print(user_form.errors, customer_form.errors)
        else:
            user_form = UserForm
            customer_form = CustomerForm()
        return render(request, 'customer_register.html', {'user_form': user_form,
                                                          'customer_form': customer_form,
                                                          'registered': registered})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if Administrator.objects.filter(user=user):
                    login(request, user)
                    return redirect(reverse('market:my_stock'))
                else:
                    login(request, user)
                    return redirect(reverse('market:stock_list'))
            else:
                print("Invalid login details: {0}, {1}".format(username, password))
        else:
            render(request, 'login.html')


class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect(reverse('market:login'))
