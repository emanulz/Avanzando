from django.db import models

# Create your models here.
class Client(models.Model):
	name=models.CharField(max_length=255,null=False)
	identification=models.IntegerField(blank=True, null=True, default="0")
	adress=models.CharField(max_length=255, default="Sin direccion registrada")	
	client_code=models.IntegerField(blank=True, default="0")
	credit_limit=models.FloatField(blank=True, default="0")
