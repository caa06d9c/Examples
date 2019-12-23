from django.http import HttpResponse


def index(request):
    return HttpResponse(request.get_full_path())
