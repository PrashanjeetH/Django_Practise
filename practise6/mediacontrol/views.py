from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .forms import PlaylistForm
from .models import Playlist
# Create your views here.

def home(request):
    return render(request, "pages/home.html")

def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = PlaylistForm(request.POST, request.FILES)
        if uploaded_file.is_valid():
            uploaded_file.save()
            return redirect('playlist_')
    else:
        uploaded_file = PlaylistForm()
    context = { 'up_data' : uploaded_file }
    return render(request, "pages/upload.html", context)

def update(request, song_id):
    context = {}
    model_instance = Playlist.objects.get(pk = song_id)
    form = PlaylistForm(instance = model_instance)
    context = {
        "song" : form
    }
    return render(request, "pages/update.html",context)

def playlist_(request):
    db = Playlist.objects.all()
    context = {
        "data" : db
    }
    return render(request, "pages/playlist_.html", context)


def delete(request, song_id):
    song = Playlist.objects.get(pk = song_id)
    song.delete()
    return HttpResponse("Deleted Successfully !")
