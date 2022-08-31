from django.forms import ModelForm
from .models import Piece, Ability

class PieceForm(ModelForm):
    class Meta:
        model = Piece
        fields = ['date', 'piece']


class AbilityForm(ModelForm):
    class Meta:
        model = Ability
        fields = ['description']