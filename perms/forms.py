from django.forms import ModelForm
from django.forms import SelectMultiple, Select

from .models import Perm


class PermForm(ModelForm):
    class Meta:
        model = Perm
        fields = '__all__'
