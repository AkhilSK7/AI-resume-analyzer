from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from resumeanalyzer.models import Resume
from resumeanalyzer.serializers import ResumeSerializer
from rest_framework.permissions import IsAuthenticated
from docx import Document
from rest_framework.views import APIView
from pypdf import PdfReader
import os
# Create your views here.

class ResumeAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ResumeSerializer
    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        resume=serializer.save(user=self.request.user)
        extracted_text = ""
        try:
            path=resume.file.path
            extension=os.path.splitext(path)[1].lower()
            if extension=='.pdf':
                reader=PdfReader(resume.file.path)
                for page in reader.pages:
                    extracted_text+=page.extract_text() or ""
            elif extension=='.docx':
                doc=Document(resume.file.path)
                for para in doc.paragraphs:
                    extracted_text+=para.text+'\n'
            else:
                raise ValidationError({"file": "Unsupported file type. Please upload PDF or DOCX."})
        except ValidationError:
            raise
        except Exception:
            raise ValidationError({"file": "Failed to read the uploaded file."})

        resume.extracted_text=extracted_text.strip()
        resume.save()



