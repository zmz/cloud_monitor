__author__ = 'zhangxg'

from django import forms

class ImageFilterForm(forms.Form):
    timestart = forms.DateTimeField(required=False)
    timeend = forms.DateTimeField(required=False)
    frequency = forms.IntegerField(required=False)
