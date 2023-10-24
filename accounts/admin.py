from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserChangeForms, UserCreationForms


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (None, {"fields": ("username", "password")}),
    #     (_("Personal info"), {"fields": ("first_name", "last_name", "email", "mobile_phone")}),
    #     (
    #         _("Permissions"),
    #         {
    #             "fields": (
    #                 "is_active",
    #                 "is_staff",
    #                 "is_superuser",
    #                 "groups",
    #                 "user_permissions",
    #             ),
    #         },
    #     ),
    #     (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    # )
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": ("username", "password1", "password2"),
    #         },
    #     ),
    # )
    # form = UserChangeForms
    # add_form = UserCreationForms
    # list_display = ("username", "email", "first_name", "last_name", "is_staff")
    # list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    # search_fields = ("username", "first_name", "last_name", "email")
    # ordering = ("username",)
    # filter_horizontal = (
    #     "groups",
    #     "user_permissions",
    # )
    ...
