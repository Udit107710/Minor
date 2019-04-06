from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as laz
from .models import Results

class Result(forms.Form):
	prediction = forms.CharField()

class PredictForm(forms.ModelForm):
	petal_length = forms.FloatField(help_text="Enter the petal length in floating point")
	petal_width = forms.FloatField(help_text="Enter the petal width in floating point")
	sepal_length = forms.FloatField(help_text="Enter the sepal length in floating point")
	sepal_width = forms.FloatField(help_text="Enter the sepal width in floating point")

	class Meta:
		model = Results
		exclude = ['prediction']
	
	def clean_petal_length(self):
		data = self.cleaned_data['petal_length']
		if data < 0 : 
			raise ValidationError(laz('Inavlid entry - negative number (petal length)'))
		return data

	def clean_petal_width(self):
		data = self.cleaned_data['petal_width']
		if data < 0 : 
			raise ValidationError(laz('Invalid entry - negative number (petal width)'))
		return data
		
	def clean_sepal_length(self):
		data = self.cleaned_data['sepal_length']
		if data < 0 : 
			raise ValidationError(laz('Invalid entry - negative number (sepal length) '))
		return data

	def clean_sepal_width(self):
		data = self.cleaned_data['sepal_width']
		if data < 0:
			raise ValidationError(laz('Invalid entry - negative number (sepal width)'))
		return data
