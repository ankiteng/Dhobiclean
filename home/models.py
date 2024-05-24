from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)  # Add this field
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
