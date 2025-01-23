from django.db import models

class Email(models.Model): 
    email = models.EmailField(unique = True)
    timestamp = models.DateTimeField(auto_now_add = True)



class EmailVerificationEvent(models.Model):
    parent = models.ForeignKey(Email, on_delete = models.SET_NULL, null = True)
    email = models.EmailField()
    expired = models.BooleanField(default = False)
    attempts = models.IntegerField(default = 0)
    last_attempt_at = models.DateTimeField(auto_now = False, auto_now_add = False, blank = True, null = True)
    expired_at = models.DateTimeField(auto_now = False, auto_now_add = False, blank = True, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)

