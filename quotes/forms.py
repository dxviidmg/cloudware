from .models import Address, Quote, Person
from django import forms


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        exclude = ['status', 'address']