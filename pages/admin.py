from django.contrib import admin
from .models import Train, Ticket, Coach

admin.site.register(Train)
admin.site.register(Ticket)
admin.site.register(Coach)