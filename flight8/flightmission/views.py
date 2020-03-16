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

