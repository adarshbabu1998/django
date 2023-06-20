from . models import *
from django.forms import ModelForm

class bookform(ModelForm):
    class meta:
        model = Book
        fields='___all___'

