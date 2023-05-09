from django import forms

class PredictionForm(forms.Form):
    distance = forms.FloatField()
    start_longitude = forms.FloatField()
    start_latitude = forms.FloatField()
    crossing_false = forms.FloatField()
    crossing_true = forms.FloatField()
    Traffic_Calming_false = forms.FloatField()
    Traffic_Calming_true = forms.FloatField()
    humidity = forms.FloatField()
    precipitation = forms.FloatField()
    give_way_false = forms.FloatField()
    give_way_true = forms.FloatField()
    stop_true = forms.FloatField()
    stop_false = forms.FloatField()
    amenity_false = forms.FloatField()
    amenity_true = forms.FloatField()
    bump_false = forms.FloatField()
    bump_true = forms.FloatField()