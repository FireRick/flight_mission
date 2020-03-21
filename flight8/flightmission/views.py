from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, permission_required

from flightmission.models import Mission, Aircraft
from .forms import MissionForm


# Create your views here.
@login_required
def index_view(request):
    missions = Mission.objects.all()
    context = {
        'missions': missions,
    }
    return render(request, 'flightmission/index.html', context=context)


@login_required
def mission_detail_view(request, mission_id):
    mission = Mission.objects.get(id=mission_id)
    context = {
        'mission': mission,
    }
    return render(request, 'flightmission/mission_detail.html', context=context)


@login_required
@permission_required(('flightmission.add_mission', 'flightmission.change_mission',
                      'flightmission.delete_mission'), raise_exception=True)
def mission_upload_view(request):
    if request.method == 'POST':
        form = MissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flightmission:mission_upload_done'))
    else:
        form = MissionForm()
    
    return render(request, 'flightmission/mission_upload.html', {'form': form})


def mission_upload_done_view(request):
    return render(request, 'flightmission/mission_upload_done.html')


@login_required
def aircraft_detail_view(request, aircraft_number):
    aircraft = Aircraft.objects.get(aircraft_number=aircraft_number)
    return render(request, 'flightmission/aircraft_detail.html', {'aircraft': aircraft})
