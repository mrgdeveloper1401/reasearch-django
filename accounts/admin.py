from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserChangeForms, UserCreationForms
from django.contrib.auth.models import Group



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("full_name", "mobile_phone", "date_of_birth")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    form = UserChangeForms
    add_form = UserCreationForms
    list_display = ("email", "full_name","is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "full_name", "email")
    ordering = ("date_joined",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

admin.site.unregister(Group)
