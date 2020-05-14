from django.shortcuts import render
from .models import Contact_models
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home/home.html', {})    #create home view


def about(request):
    return render(request, 'home/about.html', {})   #create about view


def projects(request):
    return render(request, 'home/projects.html', {})    #create home view


def skils(request):
    return render(request, 'home/skils.html', {})   #create about view


def contact(request):
    name = request.POST.get("name")                                             # create variable as request by POST
    surname = request.POST.get("surname")
    company = request.POST.get("company")
    email = request.POST.get("email")
    question = request.POST.get("question")
    confirmation = request.POST.get("confirmation")

    send = ""                                           # create empty variables and lists
    confirmation_text = ""

    if request.method == "POST":                       # create data from form (click Botton)
        Contact_models.objects.create(name=name, surname=surname, company=company, email=email, question=question)

        if confirmation == 'on':                         # if checkbox confirmation checked on/off def... variable send
            send            = 'A copy of the form has been sent to Your email address: {}'.format(email)

            subject         = 'DiddyChriss Portfolio copy of the form'                      # subject of email
            message         = 'Hello, Thank You for using DiddyChriss contact forms!'       # reserve messego
            from_email      = settings.EMAIL_HOST_USER                      # adres from send and details from settings
            recipient_list  = email                                         # delivery email
            html_message    = loader.render_to_string('emailsend.html',
                                                      {
                                                          'name': name.capitalize(),
                                                          'surname': surname.capitalize(),
                                                          'company': company.capitalize(),
                                                          'question': question
                                                      }
                                                    )     # render body from html(templates)

            send_mail(subject, message, from_email, [recipient_list], fail_silently=True, auth_user=None,
                      auth_password=None, html_message=html_message      # send_mail function
                      )
        else:
            send = ''

        confirmation_text = 'Thank You {} {} for using the contact form!'.format(name.capitalize(),
                                                                                 surname.capitalize()
                                                                                 )

    context = {
        'send'              : send,
        'confirmation_text' : confirmation_text
    }
    return render(request, 'home/contact.html', context)                #create about view



