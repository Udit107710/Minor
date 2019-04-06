from django.db import models
from django.forms import ModelForm
class Results(models.Model):
	petal_length = models.FloatField()
	petal_width = models.FloatField()
	sepal_length = models.FloatField()
	sepal_width = models.FloatField()
	prediction = models.CharField(max_length=100)

'''
class PredictForm(ModelForm):
	class Meta:
		model = Result
		exclude = ['prediction']
'''
