from django import forms
from .models import Person

class PersonForm(forms.Form):
    name_attrs = {
        'id': 'id_name',
        'type': 'text',
		'class': 'form-input',
		'placeholder': 'Masukan nama'
    }

    no_juz_attrs = {
        'id': 'id_no_juz',
        'type': 'text',
        'class': 'form-input',
        'placeholder': 'Masukan juz ke berapa'
    }

    nomer_kloter_attrs = {
        'id': 'id_nomer_kloter',
        'type': 'text',
        'class': 'form-input',
        'placeholder': 'Masukan kloter'
    }

    telepon_attrs = {
        'id': 'id_telepon',
        'type': 'text',
        'class': 'form-input',
        'placeholder': 'Masukan nomer telepon'
    }



    name = forms.CharField(required=True, widget=forms.TextInput(attrs=name_attrs))
    no_juz = forms.IntegerField(required=True, widget=forms.NumberInput(attrs=no_juz_attrs))
    nomer_kloter = forms.IntegerField(required=True, widget=forms.NumberInput(attrs=nomer_kloter_attrs))
    telepon = forms.CharField(required=True, widget=forms.TextInput(attrs=telepon_attrs))
