from django.db import models

class Collage(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='temp_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

class ImageItem(models.Model):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='collages/')