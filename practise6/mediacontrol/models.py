from django.db import models

# Create your models here.

class Playlist(models.Model):
    title = models.CharField(max_length = 256)
    genre = models.CharField(max_length = 256)
    singer = models.CharField(max_length = 256)
    mp3 = models.FileField(upload_to = 'media%H%M%S')


    class Meta:
        verbose_name_plural = 'My PlayList'
    
    def __str__(self):
        return self.title
