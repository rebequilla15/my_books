from django.db import models

# Create your models here.

title = models.CharField(max_length=250)

title = models.CharField(max_length=250)
author = models.CharField(max_length=250)
image = models.CharField(max_length=2000)
created_at =models.CharField(auto_now_add=True)
update_at = models.CharField(auto_now=True)