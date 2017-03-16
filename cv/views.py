import datetime
from django.shortcuts import render
from dateutil.relativedelta import relativedelta
from .models import Person
# Create your views here.


def person(request):
    cv = Person.objects.get(pk=1)
    show_comments = 'show_comments' in request.GET
    age = relativedelta(datetime.date.today(), cv.birthday).years
    language_levels = cv.languagelevel_set.all()
    return render(
        request, 'cv/cv.html', {
            'cv': cv,
            'age': age,
            'show_comments': show_comments,
            'language_levels': language_levels,
        })
