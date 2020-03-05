from django.db import models

# Create your models here.


class CsvData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    country = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

