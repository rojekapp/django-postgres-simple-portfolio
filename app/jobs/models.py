from django.db import models

# Create your models here.
class Job(models.Model):
    #image
    image = models.ImageField(upload_to='databasefiles/')

    #summary
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary