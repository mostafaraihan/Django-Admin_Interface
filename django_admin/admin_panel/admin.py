from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    #Fields Display
    list_display = ('Name', 'Roll', 'Technology')

    #Search Field
    search_fields = ('Roll',)

    #Filter
    list_filter = ('Name','Roll')


admin.site.register(Student, StudentAdmin)