from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index_root.html')
    context = {
        'urls': ['echo', 'db']
    }

    return HttpResponse(template.render(context, request))
