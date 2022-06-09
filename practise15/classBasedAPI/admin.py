from django.contrib import admin

from classBasedAPI.models import StudentModel
# Register your models here.
@admin.register(StudentModel)
class StudentAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_no', 'city',)