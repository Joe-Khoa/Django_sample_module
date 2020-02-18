from django import forms
from manual_app.models import ManualModel
class InputForm(forms.ModelForm):
    class Meta:
        model = ManualModel
        fields = [
            'first_name',
            'last_name',
            'roll_number',
            'password',
        ]

# ,widget = forms.TextInput(
#             attrs ={'class':'form-control'})
#
# ,widget = forms.TextInput(
#             attrs ={'class':'form-control'})
#
# ,widget = forms.TextInput(
#             attrs ={'class':'form-control'})
#
# widget = forms.PasswordInput(
#             attrs={'class':'form-control'})
