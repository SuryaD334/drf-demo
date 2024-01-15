from django.db import models

class MovieData(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/',default = 'Images/None/noimg.jpg')
    
