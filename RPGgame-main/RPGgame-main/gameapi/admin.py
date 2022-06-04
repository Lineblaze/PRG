from django.contrib import admin
from .models import Level, Hero, Boss
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Level)
class levels(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Hero)
class heroes(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Boss)
class bosses(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

