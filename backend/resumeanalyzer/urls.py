
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from resumeanalyzer import views

app_name='resumeanalyzer'
router=SimpleRouter()
router.register('resumes',views.ResumeAPIView,basename='resumes')

urlpatterns = [
    path('',include(router.urls)),
]
