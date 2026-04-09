from django.contrib import admin

# Register your models here.

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age','email')
    search_fields = ('name',)
    list_filter = ('age',)

admin.site.register(Student, StudentAdmin)

