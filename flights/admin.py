from django.contrib import admin
from .models import Airport, Flight, Passanger


class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'duration')


class PassangerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',)


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passanger, PassangerAdmin)