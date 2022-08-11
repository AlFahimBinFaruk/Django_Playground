from django.shortcuts import render, redirect
from .models import Room, User, Photos
from .forms import RoomForm, MyUserCreationForm, PhotoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("user=>", request.POST)
        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'base/login.html')


def registerUser(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    rooms = Room.objects.all()
    return render(request, "base/home.html", {"rooms": rooms})


# rooms = ['chat', 'app', 'hagnout']


def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, "base/room.html", {"room": room})

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()

    if request.method == "POST":
        # get form value one by one
        # name=request.POST.get("name")
        # get all from value at the same time
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "new room created")
            return redirect('home')
    context = {'form': form}
    return render(request, "base/room_form.html", context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        # instance = room means update the room and dont carete an new room
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "base/room_form.html", context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, "base/delete.html", {'obj': room})


def photoList(request):
    photos = Photos.objects.all()
    print("data", photos)
    return render(request, "base/photo_list.html", {"photos": photos})


def uploadPhoto(request):
    form = PhotoForm()

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "photo uploaded")
            return redirect('home')
    context = {'form': form}
    return render(request, "base/photo_form.html", context)
