from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):

#Read Operation

    #Fields Display
    list_display = ('Name', 'Roll', 'Technology',)

    #Search Field
    search_fields = ('Roll',)

    #Filter
    list_filter = ('Roll',)

    #Per Page
    list_per_page = 5

    #Ordering
    ordering = ('Roll',)


#Update Operation

    #Read Only Field
    readonly_fields = ('Technology','Roll',)



admin.site.register(Student, StudentAdmin)