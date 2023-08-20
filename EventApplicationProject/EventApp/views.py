from django.shortcuts import render, redirect
from .models import ProfileModel, EventModel
from .forms import ProfileModelForm, EventModelForm


def index_view(request):
    return render(request, 'shared/home-page.html')


def dashboard_view(request):
    profile = ProfileModel.objects.first()
    events = EventModel.objects.all()
    context = {'profile': profile, 'events': events}
    return render(request, 'events/dashboard.html', context)


def profile_create_view(request):
    if request.method == 'POST':
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = ProfileModelForm()
    context = {'form': form}
    return render(request, 'profiles/profile-create.html', context)


def profile_edit_view(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = ProfileModelForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileModelForm(instance=profile)
    context = {'profile': profile, 'form': form}
    return render(request, 'profiles/profile-edit.html', context)


def profile_delete_view(request):
    profile = ProfileModel.objects.first()
    events = EventModel.objects.all()
    if request.method == 'POST':
        events.delete()
        profile.delete()
        return redirect('index')

    context = {'profile': profile}
    return render(request, 'profiles/profile-delete.html', context)


def profile_details_view(request):
    profile = ProfileModel.objects.first()
    events = EventModel.objects.all
    context = {'profile': profile, 'events': events}
    return render(request, 'profiles/profile-details.html', context)


def event_create_view(request):
    if request.method == 'POST':
        form = EventModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventModelForm()

    profile = ProfileModel.objects.first()
    context = {'profile': profile, 'form': form}
    return render(request, 'events/event-create.html', context)


def event_edit_view(request, id):
    event = EventModel.objects.first()
    if request.method == 'POST':
        form = EventModelForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventModelForm(instance=event)
    context = {'form': form, 'event': event, 'id': id}
    return render(request, 'events/event-edit.html', context)


def event_delete_view(request, id):
    event = EventModel.objects.first()
    if request.method == 'POST':
        event.delete()
        return redirect('dashboard')
    context = {'event': event, 'id': id}
    return render(request, 'events/events-delete.html', context)


def event_details_view(request, id):
    profile = ProfileModel.objects.first()
    event = EventModel.objects.first()
    context = {'event': event, 'id': id, 'profile': profile}
    return render(request, 'events/events-details.html', context)
