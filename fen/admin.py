from django.contrib import admin
from .models import Department, Program, Teacher, HomePageContent, ExchangeProgram

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')
    search_fields = ('name', 'head')

@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ('university', 'languages', 'slots', 'deadline')
    search_fields = ('university', 'languages')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'coordinator_name')
    list_filter = ('department',)
    search_fields = ('name', 'code', 'coordinator_name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'degree', 'department')
    list_filter = ('department', 'degree')
    search_fields = ('name', 'position')

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)