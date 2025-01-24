from .models import Email, EmailVerificationEvent
from django.conf import settings
from django.core.mail import send_mail

EMAIL_HOST_USER = settings.EMAIL_HOST_USER

def verify_email(email):
    qs = Email.objects.filter(email = email, active = False)
    return qs.exists()

def get_verivication_email_msg(verivication_instance, as_html = False): 
    if not isinstance(verivication_instance, EmailVerificationEvent): 
        return None
    if as_html: 
        return f"<h1>{verivication_instance.id}</h1>"
    return f"{verivication_instance.id}"

def start_verification_event(email): 
    email_obj, created = Email.objects.get_or_create(email=email)
    obj = EmailVerificationEvent.objects.create(parent = email_obj, email = email)
    sent = send_verification_email(obj.id)
    return obj, sent


def send_verification_email(verify_obj_id):
    verify_obj = EmailVerificationEvent.objects.get(id = verify_obj_id)
    email = verify_obj.email
    subject = "Verify your email"
    from_user = EMAIL_HOST_USER
    to_user = email
    text_msg = get_verivication_email_msg(verify_obj, as_html = False)
    text_html = get_verivication_email_msg(verify_obj, as_html = True)
    return send_mail( 
        subject, 
        text_msg, 
        from_user,
        [to_user], 
        fail_silently = False, 
        html_message = text_html 
    )