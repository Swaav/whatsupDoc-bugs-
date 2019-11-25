from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketAddForm, LoginForm

def index(request):
    html = 'index.html'

    new = Ticket.objects.filter(
        ticket_stats='New').order_by('-time_date')
    in_progress = Ticket.objects.filter(
        ticket_stats='IN Progress').order_by('-time_date')
    done = Ticket.objects.filter(
        ticket_stats='Done').order_by('-time_date')
    invalid = Ticket.objects.filter(
        ticket_stats='Invalid').order_by('-time_date')

    return render(request, html, {
        'new': new,
        'in_progress': in_progress,
        'done': done,
        'invalid': invalid
        })


@login_required
def newticket_view_form(request):
   html = 'transformer.html'

   if request.method == 'POST':
        form = TicketAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                ticket_stats=data['ticket_stats'],
                user_ticket=request.user,
                assigneduser=data['assigneduser']
            )
            return HttpResponseRedirect(reverse('homepage'))

   form = TicketAddForm()

   return render(request, html, {'form': form})



@login_required
def dev_view(request, id):
    html = 'devine.html'

    created = Ticket.objects.filter(creator=id)
    assigned = Ticket.objects.filter(bloodsign=id)
    completed = Ticket.objects.filter(finisher=id)

    return render(request, html,
                  {'created': created,
                   'assigned': assigned,
                   'completed': completed})


@login_required
def ticket_view(request, id):
    html = 'ticket.html'

    ticket = Ticket.objects.filter(id=id)

    return render(request, html, {'ticket': ticket})


def login_view(request):
    html = 'transformer.html'

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get(
                        'next',
                        reverse('homepage')
                    )
                )

    form = LoginForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def edit_ticket_view(request, id):
    html = 'transformer.html'

    instance = Ticket.objects.get(id=id)

    if request.method == 'POST':
        form = TicketAddForm(
            request.POST,
            instance=instance
            )
        form.save()

        if instance.ticket_stats == 'Done':
            instance.completed_by = instance.finisher
            instance.assigned_by = None
            form.save()
        elif instance.ticket_stats == 'Invalid':
            instance.assigned_by = None
            instance.completed_by = None
            form.save()
        elif instance.ticket_stats == 'IN Progress' and instance.assigned_by is None:
            instance.assigned_by = instance.bloodsign
            instance.completed_by = None
            form.save()
        elif instance.assigned_by is not None:
            instance.ticket_stats = 'IN Progress'
            instance.completed_by = None
            form.save()

        return HttpResponseRedirect(reverse('homepage'))

    form = TicketAddForm(instance=instance)

    return render(request, html, {'form': form})

