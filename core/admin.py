from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EvangelismTeamMember, NewConvert,  Task, TaskMembers

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type', 'phone_number')}),
    )
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)

class EvangelismTeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', )
    search_fields = ('phone_number', 'full_name')
    
    class Meta:
        model = EvangelismTeamMember
    
    
admin.site.register(EvangelismTeamMember, EvangelismTeamMemberAdmin)
