from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Datalist, Contact
# Create your views here.
def index(request):
    try:
        name = Datalist.objects.all()
    except Datalist.DoesNotExist:
        raise Http404("No Names Available !")
    context = {
        "names" : name
    }
    return render(request, "pages/index.html", context)

def page1(request, name_id):
    try:
        fname_id = Datalist.objects.get(pk = name_id)
        contact = Contact.objects.get(fname = fname_id)
    except Contact.DoesNotExist:
        raise Http404("Contact details unAvailable!")
    context = {
        "detail" : contact,
        "id" : name_id
    }
    return render(request, "pages/page1.html", context)
