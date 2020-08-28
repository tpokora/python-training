from django import forms


class TrackerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    unit = forms.CharField(label='Unit', max_length=30, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', max_length=300, required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
