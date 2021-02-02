from django.contrib import admin
from core.models import Person, Student, Teacher
# Register your models here.


# admin.site.register(Person)
# admin.site.register(Student)
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['FirstName','LastName']
    list_display_links = ['LastName',]
    search_fields = ['FirstName']
    list_editable = ('FirstName',)
    list_filter = ['LastName']

@admin.register(Teacher)
class AdminStudent(admin.ModelAdmin):
    list_display = ['FirstName','LastName']
    list_display_links = ['LastName',]
    search_fields = ['FirstName']
    list_editable = ('FirstName',)
    list_filter = ['LastName']
