
from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import liste



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))      

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



def liste(request):
   
    liste= [
        {
            'name' :"COMPAORE",
           'agent_name' :"LINGANI",
           'email' :"kcompaore73@gmail.com",
           'agent_grade' :"DSI",
           'comment' :"Projet de developpement d'application",
        },
       
    ]
    if request.method == 'POST':
       
        form = liste(request.POST) 
        print("data", form.data)
        # check if it's valid:
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_agent_name = form.cleaned_data['agent_name']
            form_email = form.cleaned_data['email']
            form_agent_grade = form.cleaned_data['agent_grade']
            form_comment = form.cleaned_data['comment']
            context['info'] = {
                    'name' : form_name,
                    'agent_name' : form_agent_name,
                    'email': form_email,
                    'agent_grade' : form_agent_grade,
                    'comment': form_comment
                }
            context['btnFormHidden'] = True # To hide the button is the form is successfully submitted
            # print the values to make sure their are correct
            print(context['info'])                                                              
    
   
    return render(request,'home/author.html', context)
