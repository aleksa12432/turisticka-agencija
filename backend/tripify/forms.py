from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number']

class BookForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    PAYMENT_METHODS = [(0, 'card'), (1, 'cash')]
    payment_method = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_METHODS)
    number_of_adults = forms.IntegerField(max_value=5, min_value=1)
    number_of_children = forms.IntegerField(max_value=5, min_value=1)