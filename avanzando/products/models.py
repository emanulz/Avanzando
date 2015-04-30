from django.db import models

# Create your models here.
class Product(models.Model):
	description=models.CharField(max_length=255,null=False)
	price=models.IntegerField(blank=True, null=True, default="0")
	fractioned=models.CharField(max_length=255, default="Sin direccion registrada")	
	taxes=models.IntegerField(blank=True, default="0")
	taxes_amount=models.FloatField(blank=True, default="0")