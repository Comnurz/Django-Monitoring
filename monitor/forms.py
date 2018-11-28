from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Server


# Forms
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False,
                                help_text='Optional.')
    email = forms.EmailField(max_length=254,
                             help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2', )


class ServerForm(forms.ModelForm):
    server_name = forms.CharField(max_length=150, required=True)
    server_description = forms.CharField(required=False)

    class Meta:
        model = Server
        fields = ('server_name', 'server_description')


class ServerUpdateForm(forms.ModelForm):
    server_name = forms.CharField(max_length=150, required=False)
    server_description = forms.CharField(required=False)
    server_id = forms.IntegerField()

    class Meta:
        model = Server
        fields = ('server_name', 'server_description', 'server_id')
