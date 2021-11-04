from django.contrib import admin

from .models import ChartModel


@admin.register(ChartModel)
class ChartModelAdmin(admin.ModelAdmin):
    class Meta:
        pass
