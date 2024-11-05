from django.db import models

# Create your models here.
from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=50)  # video or image
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
