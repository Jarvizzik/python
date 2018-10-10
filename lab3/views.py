from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from . models import Song


def start(request):
	return render(request, 'playlist_app/startpage.html')
	if request.method == 'POST
def register(request):':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
	    form = UserCreationForm()
	context = {'form':form}
	return render(request,'registration/register.html',context)

def index(request):
	playlist = Song.objects.all()
	context = {'playlist':playlist} 
	return render(request, 'playlist_app/index.html',context)

def add(request):
    print(request.POST)
    song = Song(name = request.POST['name'],author = request.POST['author'],adder = request.user.username)
    song.save()
    return redirect('index')

def edit(request, id):
	song = Song.objects.get(id=id)
	context = {"song":song}
	return render(request, 'playlist_app/edit.html',context)

def update(request, id):
	song = Song.objects.get(id=id)
	song.name = request.POST['name']
	song.author = request.POST['author']
	song.save()
	return redirect('index')

def destroy(request, id):
	song = Song.objects.get(id=id)
	song.delete()
	return redirect('index')