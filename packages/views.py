from django.shortcuts import render
from .models import Package


def home(request):
    packages = Package.objects.all()
    context = {
        'packages': packages
    }
    return render(request, 'home/home.html', context=context)

