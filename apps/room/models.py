from django.db import models
from django.contrib.auth.models import User
from apps.category.models import Category  # Assuming the category app is called 'category'
from apps.city.models import City  # Assuming the city app is called 'city'
from django.conf import settings  # Assuming the settings app is called'settings'

# Facilities options
FACILITY_CHOICES = [
    ('24h_water', '24 Hours Water'),
    ('cold_water', 'Cold Water'),
    ('hot_water', 'Hot Water'),
    ('separate_bathroom', 'Separate Bathroom'),
    ('common_bathroom', 'Common Bathroom'),
]

# Allowed in room choices (number of people)
ALLOWABLE_CHOICES = [(str(i), str(i)) for i in range(1, 7)]  # 1, 2, 3, 4, 5, 6

# Floor options (Ground, 1, 2, 3,...)
FLOOR_CHOICES = [('Ground', 'Ground')] + [(str(i), str(i)) for i in range(1, 10)]  # Ground, 1, 2, ..., 9

class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    floor = models.CharField(max_length=50, choices=FLOOR_CHOICES)
    landmark = models.CharField(max_length=200)
    address = models.TextField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Relationships
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    # Room facilities
    facilities = models.CharField(max_length=200, choices=FACILITY_CHOICES, blank=True, null=True)

    # Allowable number of people
    allowable_in_room = models.CharField(max_length=2, choices=ALLOWABLE_CHOICES, default='1')

    # Light responsibility (Owner or Renter)
    light_responsibility = models.CharField(max_length=20, choices=[('Owner', 'Owner'), ('Renter', 'Renter')], default='Owner')

    # Room images (at least 3 required)
    image1 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='room_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return self.title
