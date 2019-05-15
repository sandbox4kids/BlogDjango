from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model): #name of class is Posts
    title = models.CharField(max_length=200) #field: title
    body = models.TextField() #field: body #more characters than a character field
    created_at = models.DateTimeField(default=datetime.now, blank=True) #field: created_at (time)
    def __str__ (self):
        return self.title
    class Meta:
        verbose_name_plural = "Posts"