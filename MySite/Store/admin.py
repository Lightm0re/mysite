from django.contrib import admin
from .models import ConsType, StoreItem, MoveItem, Firm


class ConsTypeAdmin(admin.ModelAdmin):
    fields = ['name']
    list = ['name']


admin.site.register(ConsType, ConsTypeAdmin)


class StoreItemAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'firm']
    list_display = ['name', 'type', 'firm']
    list_filter = ['name', 'type']
    search_fields = ['name']


admin.site.register(StoreItem, StoreItemAdmin)


class MoveItemAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'date_in', 'date_out', 'count', 'tip', 'user']
    list_display = ['name', 'type', 'date_in', 'date_out', 'count', 'tip', 'user']
    search_fields = ['type']
    list_filter = ['date_out', 'date_in']


admin.site.register(MoveItem, MoveItemAdmin)


class FirmAdmin(admin.ModelAdmin):
    fields = ['name']
    list = ['name']


admin.site.register(Firm, FirmAdmin)
