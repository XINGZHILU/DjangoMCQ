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
    physwrong = models.IntegerField(default=0)
    econwrong = models.IntegerField(default=0)
    biolsolved = models.IntegerField(default=0)
    chemsolved = models.IntegerField(default=0)
    biolwrong = models.IntegerField(default=0)
    chemwrong = models.IntegerField(default=0)
    totalsolved = models.IntegerField(default=0)
    totalwrong = models.IntegerField(default=0)
    physlast = models.DateTimeField(default='2024-06-09 00:00:00+00:00')
    econlast = models.DateTimeField(default='2024-06-09 00:00:00+00:00')
    ovrlast = models.DateTimeField(default='2024-06-09 00:00:00+00:00')
    official = models.BooleanField(default=False)
    yeargroup = models.CharField(max_length=255, default='Not assigned')
    yearselected = models.CharField(default='1' * 4095, max_length=4095)

    def __str__(self):
        return self.username


class PhysicsMCQ(models.Model):
    no = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    topic = models.CharField(max_length=64, default='unclassified')
    filename = models.CharField(max_length=64, default='placeholder.png')
    ans = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.filename


class EconomicsMCQ(models.Model):
    no = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    topic = models.CharField(max_length=64, default='unclassified')
    filename = models.CharField(max_length=64, default='placeholder.png')
    ans = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.filename

class BiologyMCQ(models.Model):
    no = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    topic = models.CharField(max_length=64, default='unclassified')
    filename = models.CharField(max_length=64, default='placeholder.png')
    ans = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.filename


class ChemistryMCQ(models.Model):
    no = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    topic = models.CharField(max_length=64, default='unclassified')
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
class BiologyStats(models.Model):
    filename = models.CharField(max_length=64, default='placeholder.png')
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)

    def __str__(self):
        return self.filename


class ChemistryStats(models.Model):
    filename = models.CharField(max_length=64, default='placeholder.png')
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)

    def __str__(self):
        return self.filename
