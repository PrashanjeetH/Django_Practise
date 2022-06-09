from django.urls import path


from classBasedAPI.views import StudentAPIView
urlpatterns = [
    path('class_based_api/student_info/', StudentAPIView.as_view(), name='get_student')
]                                                                   