from django.contrib import admin
from .models import TextEntry, DeletedTextEntry

@admin.register(TextEntry)
class TextEntryAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')

@admin.register(DeletedTextEntry)
class DeletedTextEntryAdmin(admin.ModelAdmin):
    list_display = ('text', 'deleted_at', 'deleted_by')
from django.contrib import admin

# Register your models here.
