from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProCustomers(models.Model):
    CustomerID = models.IntegerField()
    CompanyName = models.CharField(max_length=100)
    CustomerSpend = models.DecimalField(max_digits=10, decimal_places=2)
    @property
    def CustomerSpend(self):
        return "$%s" % self.CustomerSpend

    Trade = models.CharField(max_length=100)
    Zip = models.CharField(max_length=6)

	
