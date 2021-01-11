from django.http import HttpResponse
from django.template import loader
from .models import Entry


# noinspection PyUnresolvedReferences
def index(request):
    entries = list()
    result = ' '.join(q.value for q in Entry.objects.all())

    for el in result.split(' '):
        entries.append(el)

    template = loader.get_template('index_db.html')
    context = {
        'entries': entries
    }
    return HttpResponse(template.render(context, request))


# noinspection PyUnresolvedReferences
def entry(request, item):
    value = Entry.objects.get(pk=item)
    date = Entry.objects.get(pk=item).pub_date
    template = loader.get_template('entry.html')
    context = {
        'value': value,
        'date': date
    }
    return HttpResponse(template.render(context, request))
