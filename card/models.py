from django.db import models

# Create your models here.

class Card(models.Model):
    img = models.CharField(max_length=1000, unique=True)
    title = models.CharField(max_length=50, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
