from django.contrib import admin
from webapp.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_date','first_name', 'last_name','email','phone_number','address','city','county','post_code']
    
admin.site.register(Customer, CustomerAdmin)