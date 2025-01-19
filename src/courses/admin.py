from django.contrib import admin
from django.utils.html import format_html
from .models import Course,  Lesson
from cloudinary import CloudinaryImage


class LessonInline(admin.StackedInline ):
    model = Lesson 
    readonly_fields = ['updated']
    extra = 0



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['title', 'status', 'access',]
    list_filter = ['status', 'access']
    fields = ['public_id','title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['public_id','display_image']

    def display_image(self, obj, *args, **kwargs): 
        url = obj.image_admin
        return format_html(f"<img src = {url} />")
    
    display_image.short_description = "Current Image"

