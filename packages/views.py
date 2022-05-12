from django.shortcuts import render
from .models import Package
from django.views.generic import View


class Home(View):

    template_name = 'home/home.html'
    
    def get_context(self):
        wireless_packages = Package.objects.filter(type=0)
        optic_fiber_packages = Package.objects.filter(type=1)
        context = {
            'wireless_packages': wireless_packages,
            'optic_fiber_packages': optic_fiber_packages,
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context())
    