# from typing import Any
from django import forms
# from .models import Car


# class CarCreateForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         exclude = ('slug', )
        
        
# class TodoAdminForm(forms.ModelForm):
#     def clean(self):
#         title = self.cleaned_data.get('title')
#         body = self.cleaned_data.get('body')
#         if title  == 'None' or title == 'none':
#             raise forms.ValidationError({"title": "sorry title cant be none"})
#         elif body == 'None' or body == 'none':
#             raise forms.ValidationError({"body": "sorry"})
        
        
# class UpdateCarForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields = ('name', 'year')


class Serachforms(forms.Form):
    search = forms.CharField(label='search', widget=forms.TextInput)