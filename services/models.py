from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    icon_class = models.CharField(max_length=50, help_text="FontAwesome class name, e.g., fas fa-laptop-code")
    short_description = models.TextField(max_length=300)
    detailed_description = models.TextField()
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
