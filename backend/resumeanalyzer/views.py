from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.viewsets import ModelViewSet
from resumeanalyzer.models import Resume
from resumeanalyzer.serializers import ResumeSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ResumeAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ResumeSerializer
    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
