from django import forms
from antilopapp.models import Pickup,Query
User = get_user_model()


class PickupForm(forms.ModelForm):
     class Meta:
        model=pickup
        fields="__all__"

class QueryForm(forms.ModelForm):
    class Meta:
        Model=Query
        fields="__all__"

