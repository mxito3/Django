from django.db import models

# Create your models here.
## models.py
from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20) #name表示字段,CharField表示varchar
