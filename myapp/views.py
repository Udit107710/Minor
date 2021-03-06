from django.views.generic.edit import FormView
from .forms import FileFieldForm

class FileFieldView(FormView):
	form_class = FileFieldForm
	template_name = 'myapp/predict_form.html'  # Replace with your template.
	success_url = 'myapp/result.html'  # Replace with your URL or reverse().
	
	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		files = request.FILES.getlist('file_field')
		if form.is_valid():
			for f in files:
				# Do something with each file.
				print("hello")
			return self.form_valid(form)
		else:
			return self.form_invalid(form)