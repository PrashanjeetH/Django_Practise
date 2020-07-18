from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Datalist, Contact
# Create your views here.
def index(request):
    context = {
        "names" : Datalist.objects.all()
    }
    return render(request, "pages/index.html", context)

def page1(request, name_id):
    try:
        contact = Contact.objects.get(pk = name_id)
        context = {
            "contact" : contact,
            "id" : name_id,
        }
        return render(request, "pages/page1.html", context)
    except:
        raise Http404("Contact not Found!")
