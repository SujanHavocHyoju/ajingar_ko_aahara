import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#function based view
def home(request):
	#html_var = 'f strings'
	num = random.randint(0,100000)
	some_list = [num, random.randint(0,100000), random.randint(0,100000), random.randint(0,100000)]
	context = {
				"html_var":"context variable", 
				"boolean_value" : True, 
				"result":"You can pass!", 
				"num":num,
				"some_list":some_list
				}

	#return a response
	#return HttpResponse("hello")
	#return render(request, "template", {context for the template in terms of a dictionary})

	#return render(request, "base.html", {"html_var":"context variable", "boolean_value" : True, "result":"You can pass!", "num":num}) 

	return render(request, "base.html", context) 
