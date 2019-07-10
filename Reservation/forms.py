from django import forms
from .models import Reservation_Data

class RESERV_FORM(forms.ModelForm):
    class Meta:
        model = Reservation_Data
        fields = ['Group1', 'Group2', 'Author', 'Place', 'Time', 'Date']
