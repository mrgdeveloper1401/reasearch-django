# from typing import Any
# from django import forms


# class NotNoneArticleForm(forms.ModelForm):
#     def clean(self):
#         title = self.cleaned_data.get('title')
#         if title == 'None':
#             raise forms.ValidationError({"title": "cannot be None"})