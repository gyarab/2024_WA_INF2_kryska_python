from django.db import models

# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.URLField()
    country = models.CharField(max_length=100)
    background = models.URLField()
    role = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

