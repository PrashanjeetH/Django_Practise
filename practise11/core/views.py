from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView
from core.models import Student, Teacher
# Create your views here.

def Name(request):
    name = request.session
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    students = Student.objects.all()
    print(type(name))
    print(dict(name))
    context = {
        'students' : students,
        'visits' : num_visits,
    }
    return render(request, 'core/index.html', context=context)


class home(ListView):
    template_name = "core/index.html"
    context_object_name = 'home_list'
    queryset = Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        # context['students'] = Student.objects.all()
        context['teachers'] = Teacher.objects.all()
        return context
