from django.contrib import admin
from .models import team, datetime, player,competition
# Register your models here.
admin.site.register(team)
admin.site.register(player)
admin.site.register(competition)