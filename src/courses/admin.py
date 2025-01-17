from django.contrib import admin
from django.utils.html import format_html
from .models import Course 
from cloudinary import CloudinaryImage

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'access',]
    list_filter = ['status', 'access']
    fields = ['title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['display_image']

    def display_image(self, obj, *args, **kwargs): 
        print(obj.image.url)
        url = obj.image.url
        cloudinary_id = str(obj.image)
        cloudinary_hrml = CloudinaryImage(cloudinary_id).image(width = 200)

        return format_html(cloudinary_hrml)
    
    display_image.short_description = "Current Image"

