from django.db import models

# Create your models here.
class Employee(models.Model):  
    eid = models.IntegerField(primary_key=True) 
    ename = models.CharField(max_length=55)  
    eemail = models.EmailField()  
    econtact = models.PositiveIntegerField(unique=True)
    eprofilephoto = models.FileField(upload_to='profile_photo/') 
    
    
    class Meta:  
        db_table = "employees"


    
