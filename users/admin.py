from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import Group
from .models import User, Profile


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    ordering = ["email"]
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "pkid",
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "is_active",
    )
    list_display_links = ["id", "email"]
    list_filter = ("email", "username", "first_name", "last_name", "is_superuser")
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal Information",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": ("last_login", "date_joined,"),
            },
        ),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email", "username", "first_name", "last_name")


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ["user", "image"]
