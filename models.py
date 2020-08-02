from django.db import models

# Create your models here.

class Investor(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username 


class Investment(models.Model):
    INV_TYPE = (
        ('Long Term', 'Long Term'),
        ('Short Term', 'Short Term'),
    )
    PAYOUTS = (
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Half Yearly', 'Half Yearly'),
        ('Annualy', 'Annualy'),
    )
    inv_type = models.CharField(max_length=100, choices=INV_TYPE)
    inv_image = models.ImageField(upload_to = 'pics', blank=True)
    inv_per_unit = models.IntegerField(null=True)
    tenure = models.FloatField(null=True)
    payouts = models.CharField(max_length=100, null=True, choices=PAYOUTS)
    lock_in = models.IntegerField(null=True)
    return_per = models.IntegerField(null=True)
    avail_units = models.IntegerField(null=True)

    def __str__(self):
        return self.inv_type 


class Order(models.Model):
    STATUS = (
        ('In Cart', 'In Cart'),
        ('Ordered', 'Ordered'),
        ('Matured', 'Matured'),
    )
    investor = models.ForeignKey(Investor, null=True, on_delete=models.SET_NULL)
    investment = models.ForeignKey(Investment, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)    
