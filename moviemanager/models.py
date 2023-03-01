from django.db import models
import datetime

# Create your models here.
class Movies(models.Model):
    moviename = models.CharField(max_length=20)
    venuname = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    description = models.TextField()
    platinum = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    pprice = models.IntegerField(default=0)
    sprice = models.IntegerField(default=0)
    gprice = models.IntegerField(default=0)
    last_date = models.DateField()
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.moviename

class Bookings(models.Model):
    movie = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    date = models.DateField( default=datetime.date.today)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    seattype = models.CharField(max_length=20)
    totalseat = models.IntegerField()

    def __str__(self):
        return self.name





