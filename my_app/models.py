from django.db import models

# Create your models here.  
class Map(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.URLField()
    location = models.CharField(max_length=100)
    background = models.URLField()
    map_type = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
    
class Weapon(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    cost = models.IntegerField()
    fire_rate = models.CharField(max_length=100)
    magazine_size = models.IntegerField()
    description = models.TextField()
    image = models.URLField()
    alt_fire = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
    
class Text(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.URLField()
    country = models.CharField(max_length=100)
    background = models.URLField()
    role = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    map = models.ManyToManyField(Map, related_name='text')
    weapon = models.ManyToManyField(Weapon, related_name='text')

    def __str__(self):
        return self.title