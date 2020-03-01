from django.contrib import admin

from .models import Aircraft, Duty, Crew, Mission

# Register your models here.

class AircraftAdmin(admin.ModelAdmin):
    list_display = ('aircraft_type', 'aircraft_number', 'production_date',
            'init_flight_hour')


class DutyAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CrewAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name')


class MissionAdmin(admin.ModelAdmin):
    list_display = ('mission_date', 'aircraft', 'place', 'mission_type',
            'duration')

admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Mission, MissionAdmin)
