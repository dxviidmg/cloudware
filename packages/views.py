from django.shortcuts import render
from .models import Package
from django.views.generic import View
from quotes.forms import AddressForm, QuoteForm


class Home(View):
    template_name = 'home/home.html'
    
    def get_context(self):
        wireless_packages = Package.objects.filter(type=0)
        optic_fiber_packages = Package.objects.filter(type=1)
        address_form = AddressForm()
        quote_form = QuoteForm()
        context = {
            'wireless_packages': wireless_packages,
            'optic_fiber_packages': optic_fiber_packages,
            'address_form': address_form,
            'quote_form': quote_form
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context())

    def post(self, request):
        address_form = AddressForm(request.POST)
        quote_form = QuoteForm(request.POST)

        if address_form.is_valid() and quote_form.is_valid():
            address = address_form.save()
            quote = quote_form.save()
            quote.address = address
            quote.save()

        return render(request, self.template_name, self.get_context())

from django.views.generic.base import TemplateView
 
class AboutUs(TemplateView):
    template_name = 'home/aboutus.html'


class Packages(TemplateView):
    template_name = 'home/packages.html'
    
    def get_context_data(self):
        wireless_packages = Package.objects.filter(type=0)
        optic_fiber_packages = Package.objects.filter(type=1)
        context = {
            'wireless_packages': wireless_packages,
            'optic_fiber_packages': optic_fiber_packages
        }
        return context