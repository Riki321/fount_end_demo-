from django import forms
from hackthon.models import Organization,Participants

class OrganizationForms(forms.ModelForm):
    class Meta:
        model=Organization
        fields="__all__"

class ParticipantsForms(forms.ModelForm):
    class Meta:
        model=Participants
        fields="__all__"