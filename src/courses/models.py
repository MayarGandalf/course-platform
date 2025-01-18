import uuid 
from django.db import models
from django.utils.text import slugify
import helpers
from cloudinary.models import CloudinaryField
helpers.cloudinary_init()




class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"


class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"


def handle_upload(instance, filename): 
    return f"{filename}"


def get_public_id_prefix(instance, *args, **kwargs): 
    print(args, kwargs)
    title = instance.title
    if title: 
        slug = slugify(title)
        unique_id = str(uuid.uuid4()).replace("-","")[:5]
        return f"courses/{slug}-{unique_id}"
    if instance.id:
        return f"courses/{instance.id}"
    return "courses"

def get_display_name(instance, *args, **kwargs): 
    print(args, kwargs)
    title = instance.title
    if title: 
        return title
    return "Course Upload"


class Course(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(blank = True, null = True )
    image = CloudinaryField(
            "image",
            null = True, 
            public_id_prefix = get_public_id_prefix,
            display_name = get_display_name, 
            tags = ["course", "thumbnail"] 
            )
    # image = models.ImageField(upload_to = handle_upload, blank = True, null = True )
    access = models.CharField(
        max_length=5, 
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

     
    @property
    def is_published(self): 
        return self.status == PublishStatus.PUBLISHED
    
    @property
    def image_admin_url(self): 
        if not self.image:
            return ""
        image_options = { 
            "width":200
        }
        url = self.image.build_url(**image_options)
        return url 
    
    def get_image_detail(self, as_html = False, width = 500 ): 
        if not self.image:
            return ""
        image_options = { 
            "width": width
        }
        if as_html: 
            return self.image.image(**image_options)
        url = self.image.build_url(**image_options)
        return url
    

class Lesson(models.Model): 
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 120)
    description = models.TextField(blank = True, null = True)
    thumbnail = CloudinaryField("image", blank = True, null = True)
    order = models.IntegerField(default = 0)
    video  = CloudinaryField("video", blank = True, null = True, resource_type = 'video')
    can_preview = models.BooleanField(default = False, help_text = "If user does not have access to course, can they see this?" )
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices,
        default=PublishStatus.PUBLISHED
        )  
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now= True)

    class Meta: 
        ordering = ['order', '-updated']      

    