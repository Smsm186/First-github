from django.db import models

# Create your models here.


class Mail(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

