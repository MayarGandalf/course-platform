from django.shortcuts import render
from emails.forms import EmailForm 
from django.conf import settings
from emails.models import Email


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
        email_obj, created = Email.objects.get_or_create(email=email_val)

        obj = form.save()
        print(obj)
        context['form'] = EmailForm()
        context['message'] = f"Success! Check email for verification from {EMAIL_ADDRESS}"
    return render(request, template_name, context)