from django import forms
from cbv_app import models
class myForm(forms.ModelForm):
    # my_title = forms.CharField()
    # my_des = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = models.CBVModel
        fields = [
            'title',
            'description',
        ]
