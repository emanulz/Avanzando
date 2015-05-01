# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Client
#admin.site.register(Client)

class ClientAdmin(admin.ModelAdmin):
	
	
	list_display = ('name', 'identification', 'adress','email', 'hascredit')
	list_filter = ('name','identification')
	search_fields = ('name','identification')


	def hascredit(self,obj):
		return obj.credit 
			
	hascredit.admin_order_field = 'credit'
	hascredit.boolean = True
	hascredit.short_description = "Tiene crédito?"


admin.site.register(Client, ClientAdmin)
