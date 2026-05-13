from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='job-list'),
    path('<int:pk>/apply/', views.JobApplyView.as_view(), name='job-apply'),
]
