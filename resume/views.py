import datetime
from django.shortcuts import render
from dateutil.relativedelta import relativedelta
from .models import Resume
# Create your views here.


def resume(request):
    resume = Resume.objects.get(pk=1)
    show_comments = 'show_comments' in request.GET
    age = relativedelta(datetime.date.today(), resume.birthday).years
    language_levels = resume.languagelevel_set.all()
    return render(
        request, 'resume/resume.html', {
            'resume': resume,
            'age': age,
            'show_comments': show_comments,
            'language_levels': language_levels,
        })
