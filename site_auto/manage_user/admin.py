from django.contrib import admin

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from . import models

# changing Admin header
admin.site.site_header = "Site_auto Admin"

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email','nom', 'prenom', 'contact','photo','password')}),

        (_('Permissions'), {'fields': (
        'is_active', 'visiteur','staff','admin',
        'groups', 'user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','nom', 'prenom','password1', 'password2', 'contact','photo',),
        }),
    )
    list_display = ['email','nom', 'prenom', 'contact', 'staff','admin','visiteur','is_active']
    list_filter = ('staff', 'admin', 'nom','prenom')
    search_fields = ('email', 'nom','prenom')
    ordering = ('email',)
admin.site.register(models.User, UserAdmin)