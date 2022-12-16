from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    """Enables site admin to manage users"""

    model = UserProfile
    readonly_fields = ("user",)
    fields = (
        "user",
        "full_name",
        "default_phone_number",
        "default_street_address1",
        "default_street_address2",
        "default_town_or_city",
        "default_county",
        "default_postcode",
        "default_country",
    )

    list_display = (
        "user",
        "full_name",
        "date_joined",
    )
    ordering = ("full_name",)
