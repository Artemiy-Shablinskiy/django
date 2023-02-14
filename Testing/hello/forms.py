from django import forms
from .models import Contestant
class Cont_form(forms.ModelForm):
    class Meta:
        model = Contestant
        fields = ["number","time"]
