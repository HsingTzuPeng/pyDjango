from django.shortcuts import render
# from django.http import HttpResponse

from datetime import datetime

# Create your views here.


def hello(request):
    # return HttpResponse("Hello, Django.")
    return render(request, 'hello.html', {
        'current_time': str(datetime.now()),
    })
