from django.contrib import admin

from api.models import StudentsModel
# Register your models here.
@admin.register(StudentsModel)
class StudentAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_no', 'city',)