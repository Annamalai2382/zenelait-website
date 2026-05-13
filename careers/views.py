from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import JobListing, Application

class JobListView(ListView):
    model = JobListing
    template_name = 'careers/list.html'
    context_object_name = 'jobs'
    
    def get_queryset(self):
        return JobListing.objects.filter(is_active=True).order_by('-posted_on')

class JobApplyView(CreateView):
    model = Application
    template_name = 'careers/apply.html'
    fields = ['full_name', 'email', 'phone', 'resume', 'cover_letter']
    success_url = reverse_lazy('job-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = get_object_or_404(JobListing, pk=self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        job = get_object_or_404(JobListing, pk=self.kwargs['pk'])
        form.instance.job = job
        messages.success(self.request, f"Application submitted successfully for {job.title}!")
        return super().form_valid(form)
