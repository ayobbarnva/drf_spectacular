from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'is_active', 'is_admin', 'last_login')
    list_filter = ('is_active', 'is_admin')
    search_fields = ('username',)
    ordering = ('-id',)

    # فقط فیلدهایی که واقعاً در مدلت وجود داره
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('اطلاعات', {'fields': ()}),
        ('وضعیت', {
            'fields': ('is_active', 'is_admin')
        }),
        ('تاریخ‌ها', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()
    readonly_fields = ('last_login',)