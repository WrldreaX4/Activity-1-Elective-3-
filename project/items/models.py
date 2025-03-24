from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    enrolled_date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # I add New field phone number


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    