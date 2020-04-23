from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return "{}".format(self.name)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    price = models.CharField(max_length=1000000, default=0)
    quanity = models.CharField(max_length=1000000, default=0)
    picture = models.ImageField(upload_to='item_image', blank=True)
    is_removed = models.BooleanField(default=False)

    def __repr__(self):
        return "{} {} {} {} {}".format(self.category, self.name, self.price, self.quanity, self.picture)


class Stock(models.Model):
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return "{} {} {}".format(self.administrator, self.item, self.name)


class MyBug(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return "{} {} {}".format(self.customer, self.item, self.name)
