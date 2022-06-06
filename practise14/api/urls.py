from django.urls import path


from api.views import students_list
urlpatterns = [
    path('api/student_info/', students_list, name='get_student')
]                                                                   