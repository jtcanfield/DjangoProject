from django import forms

# You actually have to create a class from the forms you imported
class BMIForm(forms.Form):
    # Height in meters
    name = forms.CharField(required=False)
    height = forms.FloatField(label="Height in Meters",required=True, min_value=0)
    weight = forms.FloatField(label="Weight in Kg", required=True, min_value=0)
