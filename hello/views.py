from django.http import HttpResponse
import platform
import django

def hello_world(request):
    python_version = platform.python_version()
    django_version = django.get_version()

    return HttpResponse("Hello, World!<br>Tudo funcionando bem<br>"
                        "--Python Version: {}<br>"
                        "--Django Version: {}".format(python_version, django_version))
