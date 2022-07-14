from pyexpat import model
from random import choices
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    state_choice = (
        ('GJ','Gujarat'),
        ('MP','Madhya Pradesh'),
        ('KN','Karnataka'),
        ('MH','Maharastra'),
        ('RJ','Rajasthan'),
        ('PN','Punjab'),
    )
    year_choice = []
    for r in range(2000,(datetime.now().year+1)):
        year_choice.append((r,r))
    features_choice = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice,max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photo/%y/%m/%d/')
    car_photo1 = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)
    car_photo2 = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)
    car_photo3 = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)
    car_photo4 = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)
    features = MultiSelectField(choices=features_choice)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.IntegerField()
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return f"{self.car_title}({self.year})"


class Inquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    comments = RichTextField()
    created_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return f"{self.first_name}({self.city})"