from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView
from core.models import Student, Teacher
from datetime import datetime, timezone
# Create your views here.

def Name(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    students = Student.objects.all()
    context = {
        'students' : students,
        'visits' : num_visits,
    }
    # del request.session['num_visits']
    return render(request, 'core/index.html', context=context)


class home(ListView):
    template_name = "core/index.html"
    context_object_name = 'home_list'
    queryset = Student.objects.all() # can be accessed with object_list while template rendering
    # queryset = Student.objects.order_by('date_created')  # Use (-date_created) for descending ordering
    # queryset = Student.objects.filter(publisher__name='Goutam')

    title = "This is Title"


    # custom module returning objects for rendering
    def Teachers(self, **kwargs):
        return Teacher.objects.all()

    def Session_data(self, **kwargs):
        # returns the num_visits value or sets 0 as default
        num_visits = self.request.session.get('num_visits', 0)
        difference = self.request.session.get('difference', 0)
        self.request.session['num_visits'] = num_visits + 1
        difference = self.request.session.get_expiry_date() - datetime.now(timezone.utc)
        self.request.session['difference'] = difference.days
        return self.request.session

    # def get_context_data(self,**kwrgs):
    #     context = super().get_context_data(**kwargs)
    #     context['key'] = "value"  # Static
    #     context['object'] = ModelClassName.objects.all()   # Object
    #     return context


class PassCheck(TemplateView):
    template_name = "core/passcheck.html"
    title = "Pass Check File"
