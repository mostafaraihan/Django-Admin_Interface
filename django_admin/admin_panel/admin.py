from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    #Fields Display
    list_display = ('Name', 'Roll', 'Technology')

    #Search Field
    search_fields = ('Name','Roll')


admin.site.register(Student, StudentAdmin)