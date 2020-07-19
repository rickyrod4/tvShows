from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def allShows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request,'allShows.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
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