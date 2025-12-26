from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Roll', 'Technology')
    search_fields = ('Roll',)
    list_filter = ('Roll',)
    list_per_page = 10

admin.site.register(Student, StudentAdmin)