from django.contrib import admin
from .models import Results

class ResultsAdmin(admin.ModelAdmin):
	model = Results
	list_display = ('petal_length', 'petal_width', 'sepal_length', 'sepal_width')
	list_filter = ['prediction']

admin.site.register(Results, ResultsAdmin)
