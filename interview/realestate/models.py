from django.db import models

class Apartment(models.Model):
    city = models.CharField(max_length=100)
    rent = models.IntegerField()
    bedrooms = models.IntegerField()
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}, ₹{self.rent}, {self.bedrooms}BHK"
