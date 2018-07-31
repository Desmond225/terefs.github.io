from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:400]

    def pub_date_pretty(self):
        return self.created_on.strftime('%e %b - %Y')





#add blog models

#add to blog app settings

#create migration

#migrate

#add to admin
