from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('bookingnumber', 'status',)
        

class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Numéro de carte', widget=forms.TextInput(attrs={'placeholder': '1234 5678 9012 3456'}))
    expiration_date = forms.CharField(label='Date d\'expiration', widget=forms.TextInput(attrs={'placeholder': 'MM/AA'}))
    cvv = forms.CharField(label='CVV', widget=forms.TextInput(attrs={'placeholder': '123'}))
    # Champs supplémentaires
    name = forms.CharField(label='Nom du titulaire de la carte', max_length=100)
    email = forms.EmailField(label='Adresse e-mail')
    amount = forms.DecimalField(label='Montant du paiement', max_digits=10, decimal_places=2)


