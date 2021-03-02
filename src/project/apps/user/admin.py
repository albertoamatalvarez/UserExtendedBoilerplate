import copy

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from project.apps.user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        fieldsets = copy.deepcopy(super(UserAdmin, self).get_fieldsets(request, obj))
        fieldsets += (
            ('Perfil', {
                'fields': ['birth_date']}),
        )
        return fieldsets
