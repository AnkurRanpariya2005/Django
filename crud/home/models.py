from django.db import models

class entry(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    data1 = models.CharField(max_length=100)
    data2 = models.CharField(max_length=100)

    def __str__(self):
        return self.data1