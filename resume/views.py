import datetime
from django.shortcuts import render
from dateutil.relativedelta import relativedelta
from .models import Resume
# Create your views here.


def resume(request):
    resume = Resume.objects.get(pk=1)
    age = relativedelta(datetime.date.today(), resume.birthday).years
    return render(
        request, 'resume/resume.html', {'resume': resume, 'age': age})
