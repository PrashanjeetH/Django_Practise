from django.shortcuts import render
from .forms import InputForm
from .models import Product

# Create your views here.
def home_view(request):
	context = {}
	form = InputForm()
	if request.method == "POST":
		form = InputForm(request.POST)
		if form.is_valid():
			Product.objects.create(**form.cleaned_data)
			print(form.cleaned_data)
			form = InputForm()
		else:
			print(form.errors)
	context['form'] = form
	return render(request, "pages/home.html", context)
