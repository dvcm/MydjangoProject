
from django.shortcuts import render


def index(request):
    return render(request, 'poll/index.html', context={'hello': 'hello  world'})
