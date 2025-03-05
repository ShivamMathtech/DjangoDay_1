from django.db import models

# Create your models here.
class LoginForms(models.Model):
    name = models.CharField(max_length=100)
    password=models.CharField(max_length=40)
    date_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
