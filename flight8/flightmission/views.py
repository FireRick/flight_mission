from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from flightmission.models import Mission


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
