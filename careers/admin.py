from django.contrib import admin
from .models import JobListing, Application

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'job_type', 'is_active')
    list_filter = ('job_type', 'is_active', 'department')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'applied_at')
    readonly_fields = ('full_name', 'email', 'phone', 'resume', 'cover_letter', 'applied_at')
