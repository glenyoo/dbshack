from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'company_id', 'is_staff')
    list_filter = ('is_staff', 'groups')

    fieldsets = (
        (None, {'fields': ('username', 'password', 'company_id')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'company_id', 'password1', 'password2', 'is_staff')}
        ),
    )

    search_fields = ('username', 'company_id')
# Register the CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)
