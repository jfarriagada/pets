from django import forms

from .models import Pet

class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('nickname', 'name', 'photo', 'votes')