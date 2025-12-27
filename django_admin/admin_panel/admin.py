from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Roll', 'Technology')

admin.site.register(Student, StudentAdmin)