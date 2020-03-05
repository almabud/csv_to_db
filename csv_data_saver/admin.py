from django.contrib import admin

# Register your models here.
from csv_data_saver import models

admin.site.register(models.CsvData)
