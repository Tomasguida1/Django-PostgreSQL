from django.db import models

class game(models.Model):
    vgame_name = models.CharField(max_length=30)
    developer_name = models.CharField(max_length=30)
    year = models.IntegerField
    description = models.TextField
    categories = models.CharField
    
