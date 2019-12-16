from django import forms
from dummyapp.models import Imagemodel
class Imageform(forms.ModelForm):
    class Meta:
        model=Imagemodel
        fields=['name','email','image']
