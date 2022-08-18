from django.db import models

class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    image1 = models.ImageField(upload_to="")