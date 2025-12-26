from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no')
    search_fields = ('roll_no',)
    list_filter = ('roll_no',)
    list_per_page = 10
    list_max_show_all = 20


admin.site.register(Student, StudentAdmin)