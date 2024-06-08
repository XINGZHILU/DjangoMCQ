from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Record(models.Model):
    username = models.CharField(max_length=255)
    physics = models.CharField(default='0' * 4095, max_length=4095)
    economics = models.CharField(default='0' * 4095, max_length=4095)
    currentphys = models.IntegerField(default=0)
    currentecon = models.IntegerField(default=0)
    physsolved = models.IntegerField(default=0)
    econsolved = models.IntegerField(default=0)
    totalsolved = models.IntegerField(default=0)
    physlast = models.DateTimeField(default='2024-06-09 00:00:00+00:00')
    econlast = models.DateTimeField(default='2024-06-09 00:00:00+00:00')
    ovrlast = models.DateTimeField(default='2024-06-09 00:00:00+00:00')

    def __str__(self):
        return self.username


class PhysicsMCQ(models.Model):
    no = models.IntegerField(default=0)
    filename = models.CharField(max_length=64, default='placeholder.png')
    ans = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.filename


class EconomicsMCQ(models.Model):
    no = models.IntegerField(default=0)
    filename = models.CharField(max_length=64, default='placeholder.png')
    ans = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.filename


class PhysicsStats(models.Model):
    filename = models.CharField(max_length=64, default='placeholder.png')
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)

    def __str__(self):
        return self.filename


class EconomicsStats(models.Model):
    filename = models.CharField(max_length=64, default='placeholder.png')
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)

    def __str__(self):
        return self.filename
