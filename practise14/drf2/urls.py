from django.urls import URLPattern, path
from drf2.views import student_detail, student_list, student_create

urlpatterns = [
    path('student_info/<int:pk>', student_detail, name='student_detail'),
    path('student_info/', student_list, name='student_list'),
    path('student_create/', student_create, name='student_create'),
]