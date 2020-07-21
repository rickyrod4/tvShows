from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def allShows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request,'allShows.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = Show.objects.validate(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    Show.objects.create(
        title = request.POST['title'], 
        network = request.POST['network'],
        releaseDate = request.POST['releaseDate'],
        description = request.POST['description']
    )
    return redirect('/shows')

def show(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request,'showInfo.html',context)

def delete(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')

def edit(request, show_id):
    context = {
    'show' : Show.objects.get(id=show_id)
    }
    return render(request,'edit.html', context)

def updateShow(request, show_id):
    show = Show.objects.get(id=show_id)
    if len(request.POST['title']) > 1:
        show.title = request.POST['title']
    if len(request.POST['network']) > 1:
        show.network = request.POST['network']
    if len(request.POST['description']) > 1:
        show.description = request.POST['description']
    if len(request.POST['title']) > 1:
        show.releaseDate = request.POST['releaseDate']
    show.save()
    return redirect('/shows')