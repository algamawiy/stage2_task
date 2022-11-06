from django.db import models

# Create your models here.

class Arithmetic(models.Model):
    
    operators = (
        ('addition','addition'),
        ('subtraction', 'subtraction'),
        ('multiplication', 'multiplication')
        )
    operation_type = models.CharField(max_length=30, choices=operators)
    x = models.IntegerField()
    y = models.IntegerField()
    
    
    
    
