from django.shortcuts import render
from .models import Package


def home(request):
    wireless_packages = Package.objects.filter(type=0)
    optic_fiber_packages = Package.objects.filter(type=1)
    context = {
        'wireless_packages': wireless_packages,
        'optic_fiber_packages': optic_fiber_packages,
    }
    return render(request, 'home/home.html', context=context)
    