from django.contrib import admin
from core.models import StudentModel
# Register your models here.


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'roll_no']
