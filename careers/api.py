from rest_framework import serializers, viewsets
from .models import JobListing

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = '__all__'

class JobListingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobListing.objects.filter(is_active=True)
    serializer_class = JobListingSerializer
