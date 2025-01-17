from django.db import models
import helpers
from cloudinary.models import CloudinaryField

helpers.cloudinary_init()




class AccessRequirement(models.TextChoices): 
    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT =  "draft", "Draft"

class PublishStatus(models.TextChoices): 
    ANYONE = "any", "anyone"
    EMAIL_REQUIRED = "email", "Enail required"

def handle_upload(instance, filename): 

    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(blank = True, null = True )
    image = CloudinaryField("image", null = True )
    # image = models.ImageField(upload_to = handle_upload, blank = True, null = True )
    access = models.CharField(
        max_length = 5,
        choices = AccessRequirement.choices, 
        default = AccessRequirement.DRAFT
     )  
    status  = models.CharField(
        max_length = 10,
        choices = PublishStatus.choices, 
        default = PublishStatus.EMAIL_REQUIRED
     )
    @property
    def is_published(self): 
        return self.status == PublishStatus.PUBLISHED
    
    