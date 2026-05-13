from django.db import models

class JobListing(models.Model):
    JOB_TYPE_CHOICES = (
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('C', 'Contract'),
        ('I', 'Internship'),
    )
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='Chennai, India')
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES, default='FT')
    description = models.TextField()
    requirements = models.TextField(help_text="List bullet points or structured description")
    posted_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.department})"

class Application(models.Model):
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name="applications")
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} for {self.job.title}"
