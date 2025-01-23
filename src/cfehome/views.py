from django.shortcuts import render
from emails.forms import EmailForm 
from django.conf import settings
from emails.models import Email, EmailVerificationEvent
from emails import services as emails_services

EMAIL_ADDRESS = settings.EMAIL_ADDRESS

def home_view(request, *args, **kwargs):
    template_name = "home.html"
    form = EmailForm(request.POST or None)
    context = { 
        "form": form, 
        "message": "" 
    }
    if form.is_valid():
        email_val = form.cleaned_data.get('email')
        obj = emails_services.start_verification_event(email_val)
        print(obj)
        context['form'] = EmailForm()
        context['message'] = f"Success! Check email for verification from {EMAIL_ADDRESS}"
    else: 
        print(form.errors)
    return render(request, template_name, context)