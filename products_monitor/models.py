from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import datetime
from django.conf import settings

class CustomUser(AbstractUser):
    discord = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Brand(models.Model):
    name = models.CharField(max_length=200)
    logo_url = models.URLField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    SKU = models.CharField(max_length=200)
    instock = models.BooleanField()
    picture_url = models.URLField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    #restock_date = models.DateTimeField('date restocked')
    restock = models.BooleanField()
    original_release_date = models.DateTimeField('original release date')
    #watchers = models.IntegerField(default=0)
    discordChannelLink = models.URLField()
    channelWebhook = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def was_released_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.original_release_date <= now

class ProductKeyWord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=200)

class SavedProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
