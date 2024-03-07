from django.db import models

class Customer(models.Model):
    
    first_name = models.CharField(max_length = 92)
    last_name = models.CharField(max_length = 92)
    email = models.CharField(max_length = 92)
    phone_number= models.CharField(max_length = 15)
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 200)
    county= models.CharField(max_length = 300)
    post_code= models.CharField(max_length = 12, default='')
    created_date = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return self.first_name + " "+self.last_name
    
    