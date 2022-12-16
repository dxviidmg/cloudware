from django.shortcuts import render
from .models import Package
from django.views.generic import View
from quotes.forms import AddressForm, QuoteForm


class Cotiza(View):
    template_name = 'cotiza.html'
    
    def get_context(self):
        address_form = AddressForm()
        quote_form = QuoteForm()
        context = {
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