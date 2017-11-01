from django import forms

# You actually have to create a class from the forms you imported
class BMIForm(forms.form):
    # Height in meters
    name = forms.CharField(required=False)
    height = forms.FloatField(required=True, min_value=0)
    weight = forms.FloatField(required=True, min_value=0)
