from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return "{}".format(self.name)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=0)
    quanity = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='item_images', blank=True)
    is_removed = models.BooleanField(default=False)

    def __repr__(self):
        return "{} {} {} {} {}".format(self.category, self.name, self.price, self.quanity, self.picture)


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=datetime.now)
    avatar = models.ImageField(upload_to='admin_profile_images', blank=True)

    def __repr__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=datetime.now)
    avatar = models.ImageField(upload_to='customer_profile_images', blank=True)

    def __repr__(self):
        return self.user.username


class Stock(models.Model):
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return "{} {} {}".format(self.administrator, self.item, self.name)


class MyBug(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buy_time = models.DateTimeField(default=datetime.now)

    def __repr__(self):
        return "{} {} {}".format(self.customer, self.item, self.buy_time)
