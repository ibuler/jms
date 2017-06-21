from django.forms import ModelForm
from django.forms import TextInput, PasswordInput
from .models import Asset


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        widgets = {
            'hostname': TextInput(attrs={'placeholder': 'Hostname'}),
            'ip': TextInput(attrs={'placeholder': 'IP'}),
            'port': TextInput(attrs={'placeholder': 'Port'}),
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
        }
