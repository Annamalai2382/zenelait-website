from django.contrib import admin
from .models import ContactMessage, Testimonial

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at', 'is_read')
    list_filter = ('is_read', 'sent_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'sent_at')

admin.site.register(Testimonial)
