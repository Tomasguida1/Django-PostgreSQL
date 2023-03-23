from django.db import models

class game(models.Model):
    vgame_name = models.CharField(max_length=30)
    img = models.CharField(max_length=200)
    developer_name = models.CharField(max_length=30)
    year = models.IntegerField
    description = models.TextField(max_length=500)
    categories = models.CharField(max_length=100)
    
