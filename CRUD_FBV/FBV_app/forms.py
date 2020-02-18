from django import forms
from FBV_app.models import GeeksModel


class GeeksForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'class':'col-title'})),
    # description = forms.CharField(widget=forms.TextInput(attrs={'class':'col-des'})),
    class Meta:
        model = GeeksModel
        fields = [
                'title',
                'description',
        ]
        # widgets = {
        #     'title': forms.TextInput(attrs={}),
        #     'description': forms.TextInput(attrs={}),
        # }
