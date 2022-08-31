from django.forms import ModelForm
from .models import Ability

class AbilityForm(ModelForm):
    class Meta:
        model = Ability
        fields = ['description']