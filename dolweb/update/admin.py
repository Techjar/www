# Copyright (c) 2018 Dolphin Emulator Website Contributors
# SPDX-License-Identifier: MIT

from django.contrib import admin
from dolweb.update.models import UpdateTrack


class UpdateTrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'version')
    ordering = ('-version__date', 'name')
admin.site.register(UpdateTrack, UpdateTrackAdmin)
