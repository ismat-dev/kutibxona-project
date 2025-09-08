from django import forms

from .models import Author, Book

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class SearchForm(forms.Form):
    q = forms.CharField(max_length=120, label='Search', required=False)

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

