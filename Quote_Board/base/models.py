from django.db import models

# Create your models here.

class Quote(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    date = models.DateField()

    def __str__(self) -> str:
        return self.author
