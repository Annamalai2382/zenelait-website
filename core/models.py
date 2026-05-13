from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.name} - {self.email}"

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)

    def __str__(self):
        return f"Testimonial by {self.client_name}"
