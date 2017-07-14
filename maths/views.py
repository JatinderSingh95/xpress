from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse
import random
from django import template
from app_filters import register
from .form import userform
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404




lvl =''


def example_view(request):
        
        return render(request, 'server_list.html')

	
	
	
def division_intro(request,template_name='DIV.html'):
			
	numone = (request.GET.get('num11', None))
	numtwo = (request.GET.get('num12', None))
	numque = (request.GET.get('que', None))
	
	num = int(numone)
	num2 = int(numtwo)
	numq = int(numque) + 1
	
	f=open('DIV' + str(lvl) + '.txt','w')
	
	
	for k in range(1, 11):  ## k is the Number of pages in the sheet
			ans = ''
			for i in range(1, numq):  ## i is the Number of questions in one sheet

				j = random.randint(1, num)
				l = random.randint(1, num2)

				ans = ans + '\t' + '(' + str(i) + ')' + str(l) + '\n'

				numspace = 7 - len(str(i))  ## this is to keep the alignment of the questions after the question number
				spaces = ' ' * numspace
				if (i % 2 == 0):
					f.write ('\t' * 6 + '(' + str(i) + ')' + spaces + str(j) + ' X ' + ' _____     =   ' + str(j * l) + '\n')
				else:
					f.write ('(' + str(i) + ')' + spaces + str(j) + ' X ' + '  _____     =   ' + str(j * l))

				if (i == numq - 1):
					f.write ('\n  Answer sheet  \n')
					f.write (ans)
					
					
					
	return render(request, template_name)
		
