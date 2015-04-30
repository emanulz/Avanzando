from django.db import models
from product_categories.models import Product_Category

# Create your models here.
class Product(models.Model):
	product_code = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	price = models.PositiveIntegerField(default=0)
	fractioned = models.BooleanField(default=1,blank=True)	
	taxes = models.BooleanField(default=1,blank=True)
	taxes_amount = models.FloatField(default=0,blank=True)	
	inventory_amount = models.IntegerField(default=0,blank=True)
	inventory_minimum = models.IntegerField(default=0,blank=True)
	category = models.ForeignKey(Product_Category, default=1)

	def __unicode__(self):
		return self.description
