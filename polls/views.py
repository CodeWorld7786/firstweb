from django.http import HttpResponse


def index(request):
    return HttpResponse("<input type='password' />")