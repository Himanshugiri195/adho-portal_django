from django.db import models

# Create your models here.

class Testlist(models.Model):
    name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    
    

class Cussel(models.Model):
    salesorg = models.CharField( max_length=50)
    importzone = models.CharField( max_length=50)
    soldto = models.CharField( max_length=50)
    shipto = models.CharField( max_length=50)
    shiptoname = models.CharField( max_length=50)
    shiptocountry = models.CharField( max_length=50)
    shipcond = models.CharField( max_length=15)
    payer = models.CharField( max_length=50)
    payername = models.CharField( max_length=50)
    profitcen = models.CharField( max_length=50)
    incoterm = models.CharField( max_length=50)
    currency = models.CharField( max_length=50)
    attri = models.CharField( max_length=50)
    
    def __str__(self):
        return self.soldto
        
    

class Skusel(models.Model):
    sku = models.CharField(max_length=15)
    matdesc = models.CharField(max_length=50)
    brand = models.CharField(max_length=15)
    contsize = models.CharField(max_length=15)
    secondpack = models.CharField(max_length=15)
    
    def __str__(self):
        return self.sku
    