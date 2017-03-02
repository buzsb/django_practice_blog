from django.shortcuts import render
from .models import Resume
# Create your views here.


def resume(request):
    resume = Resume.objects.get(pk=1)
    return render(request, 'resume/resume.html', {'resume': resume})
