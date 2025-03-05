from django.contrib import admin
from .models import LoginForms
# Register your models here.
class LoginFormsAdmin(admin.ModelAdmin):
    list_display=['name','password']

admin.site.register(LoginForms,LoginFormsAdmin)