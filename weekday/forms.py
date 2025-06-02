from django import forms
from django.core.validators import RegexValidator
import calendar

class RealWeekDay(forms.Form):
    numeric_validator = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

    year = forms.CharField(
        label='Year',
        min_length=1,
        max_length=4,
        validators=[numeric_validator],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '4', 'placeholder': 'YYYY'})
    )

    monthCHOICES = [(i, calendar.month_name[i]) for i in range(1, 13)]
    dayCHOICES = [(i, str(i)) for i in range(1, 32)]

    month = forms.ChoiceField(label='Month', choices=monthCHOICES,
                              widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'id_month'}))

    day = forms.ChoiceField(label='Day', choices=dayCHOICES,
                            widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'id_day'}))


