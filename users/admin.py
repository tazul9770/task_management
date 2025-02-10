from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),  # ✅ `bio` এবং `profile_image` সরানো হলো
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # ✅ এখানে কমা যোগ করা হলো
            'fields': ('username', 'email')
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-username',)
