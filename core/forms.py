from django import forms
from core.models import BmiMeasurement

# You actually have to create a class from the forms you imported
class BMIForm(forms.Form):
    # Height in meters
    name = forms.CharField(required=False)
    height = forms.FloatField(label="Height in Meters",required=True, min_value=0)
    weight = forms.FloatField(label="Weight in Kg", required=True, min_value=0)

class BMIMeasurementForm(form.ModelForm):
    class meta:
        model = BmiMeasurement
        fields = [height_in_meters, weight_in_kg, measured_at]
