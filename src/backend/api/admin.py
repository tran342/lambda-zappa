from django.contrib import admin

from api.models import RiskType, DataField


@admin.register(DataField)
class DataFieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_required', 'field_type']


@admin.register(RiskType)
class RiskTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'fields']
    filter_horizontal = ('fields',)
