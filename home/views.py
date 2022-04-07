"""Home Views"""
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def faqs(request):
    """ A view to return the FAQ's page """

    return render(request, 'home/faqs.html')


def contact(request):
    """ A view to return the Contact Us page """
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['emailaddress']
        message = request.POST['message']

        send_mail('message from ' + message_name,
                  message + ' reply to this message ' + message_email,
                  message_email,
                  ['fullstacksteve18@gmail.com'])
        messages.success(request,
                         'Email received. We will contact you shortly.')
        return render(request, "home/contact.html")
    else:
        return render(request, "home/contact.html")
