from django import forms


class TrackerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    unit = forms.CharField(label='Unit', max_length=10, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', max_length=300, required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))


class RecordForm(forms.Form):
    value = forms.FloatField(label='Value', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    datetime = forms.DateTimeField(label='Datetime', required=True, input_formats=['%Y-%m-%d %H:%M', '%Y-%m-%d'],
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD (HH:MM)'}))
