from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Voter

@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    search_fields = ('name', 'epic_no', 'relation_name', 'door_no')
    list_display = ('name', 'epic_no', 'age', 'gender', 'door_no')
