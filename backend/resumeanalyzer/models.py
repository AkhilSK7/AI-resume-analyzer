from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='resumes')
    file=models.FileField(upload_to='resumes/')
    extracted_text=models.TextField(blank=True)
    sections=models.JSONField(default=dict,blank=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume {self.id} of {self.user.username}"