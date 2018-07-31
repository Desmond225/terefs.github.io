from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    detail = models.TextField(max_length=999, default='default values')

class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def pub_date_pretty(self):
        return self.created_on.strftime('%b %e %Y')
