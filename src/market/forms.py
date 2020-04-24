from django import forms
from django.contrib.auth.models import User
from market.models import Category, Item, Administrator, Customer, Stock, MyBug


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Please enter the category name.")

    class Meta:
        model = Category
        fields = ('name',)


class ItemForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Please enter the name of the Item.")
    price = forms.IntegerField(max_value=1000000, help_text="Please enter the price of the Item.")
    quanity = forms.IntegerField(max_value=1000000, help_text="Please enter the quanity of the Item.")
    is_removed = forms.BooleanField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Item
        exclude = ('category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ('avatar',)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('avatar',)


class StockForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Please enter the Stock name.")

    class Meta:
        model = Stock
        exclude = ('administrator', )
