import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.


# Template Based Views
class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		num = random.randint(0,100000)
		some_list = [num, random.randint(0,100000), random.randint(0,100000), random.randint(0,100000)]
		context = {
					"html_var":"context variable", 
					"boolean_value" : True, 
					"result":"You can pass!", 
					"num":num,
					"some_list":some_list
					}
		#print(context)
		return context

class ContactView(TemplateView):
	template_name = "contact.html"

class AboutView(TemplateView):
	template_name = "about.html"


# Function based view
# def home(request):
# 	#html_var = 'f strings'
# 	num = random.randint(0,100000)
# 	some_list = [num, random.randint(0,100000), random.randint(0,100000), random.randint(0,100000)]
# 	context = {
# 				"html_var":"context variable", 
# 				"boolean_value" : True, 
# 				"result":"You can pass!", 
# 				"num":num,
# 				"some_list":some_list
# 				}

	#return a response
	#return HttpResponse("hello")
	#return render(request, "template", {context for the template in terms of a dictionary})

	#return render(request, "base.html", {"html_var":"context variable", "boolean_value" : True, "result":"You can pass!", "num":num}) 

# 	return render(request, "home.html", context) 

# def about(request):
# 	context = {
# 			}
# 	return render(request, "about.html", context) 

# def contact(request):
# 	context = {
# 			}
# 	return render(request, "contact.html", context) 

# Class Based Views
# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		context = {}
# 		return render(request, "contact.html", context)

	# def post(self, request, *args, **kwargs):
	# 	context = {}
	# 	return render(request, "contact.html", context)
	
	# def put(self, request, *args, **kwargs):
	# 	context = {}
	# 	return render(request, "contact.html", context)



		
