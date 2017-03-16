import datetime
from django.shortcuts import render
from dateutil.relativedelta import relativedelta
from .models import Person
# Create your views here.


def person(request):
    person = Person.objects.get(pk=1)
    show_comments = 'show_comments' in request.GET
    age = relativedelta(datetime.date.today(), person.birthday).years
    language_levels = person.languagelevel_set.all()
    return render(
        request, 'resume/resume.html', {
            'person': person,
            'age': age,
            'show_comments': show_comments,
            'language_levels': language_levels,
        })
