from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ContactMessage, Testimonial
from services.models import Service
from blog.models import Post

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_services'] = Service.objects.all()[:4]
        context['latest_posts'] = Post.objects.filter(is_published=True)[:3]
        context['testimonials'] = Testimonial.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactView(CreateView):
    model = ContactMessage
    template_name = 'core/contact.html'
    fields = ['name', 'email', 'subject', 'message']
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        messages.success(self.request, "Your message has been successfully submitted. We'll get back to you soon.")
        return super().form_valid(form)
