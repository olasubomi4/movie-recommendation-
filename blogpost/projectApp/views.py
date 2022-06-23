from django.shortcuts import render

# Create your views here.

def error_404_view(request, exception):
# we add the path to the the 404.html file
	# here. The name of our HTML file is 404.html
	return render(request, '404.html')
