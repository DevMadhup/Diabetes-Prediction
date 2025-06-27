from django import forms

class DiabetesForm(forms.Form):
    Pregnancies = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Glucose = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    BloodPressure = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    BMI = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
