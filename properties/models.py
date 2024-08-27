from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = (
        
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        
    )

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    number_of_units = models.IntegerField(default=1)
    
    rental_cost = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name


class Tenant(models.Model):
    property = models.ForeignKey(Property, related_name='tenants', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    contact_details = models.CharField(max_length=255)
    
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RentalPayment(models.Model):
    
    tenant = models.ForeignKey(Tenant, related_name='payments', on_delete=models.CASCADE)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    payment_date = models.DateField()
    
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return  f"{self.tenant.name} - {self.payment_date} - {'Paid' if self.is_paid else 'Unpaid'}"