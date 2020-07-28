from django import forms


class WeatherStatisticsForm(forms.Form):
    latitude = forms.FloatField(required=True)
    longitude = forms.FloatField(required=True)
    start = forms.DateField(input_formats=['%Y-%m-%d'], required=False)
    end = forms.DateField(input_formats=['%Y-%m-%d'], required=False)